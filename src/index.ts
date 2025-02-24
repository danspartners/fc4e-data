import { initIndex, esClient } from './client'
import { mappings } from './mappings'
import fs from 'fs-extra'

const theIndex = 'fc4e'
const localJSONPath = 'data/data.json' // Path to local JSON file
const countryJSONPath: any = 'data/countries.json' 

export async function indexJSON() {
	await initIndex(theIndex, mappings)

	// Load JSON file
	let jsonData: any[] = []
	let countries: any = {}
	try {
		const fileContent = fs.readFileSync(localJSONPath, 'utf-8')
		const countryContent = fs.readFileSync(countryJSONPath, 'utf-8')
		jsonData = JSON.parse(fileContent) // Parse JSON
		countries = JSON.parse(countryContent) // Parse JSON
	} catch (error) {
		console.log('[ERROR] reading JSON file', error)
		return
	}

	console.log('Loaded JSON data:', jsonData.length, 'records')

	if (jsonData.length === 0) {
		console.log('No data to index')
		return
	}

	// Add lat/lng for countries
	const jsonCountryData = jsonData.map((doc) => {
		if (doc.countries) {
			const newCountries = doc.countries.map((country: any) => {
				const locationData = countries[country.iso.toUpperCase()];
				if (!locationData) {
					console.warn(`No location data for ISO: ${country.iso}`);
					return country; // Keep original if no match
				}
				return {
					...country,
					location: locationData,
				};
			});
			return ({
				...doc,
				countries: newCountries
			})
		}
		return doc;
	});

	// Prepare bulk request
	const bulkOps = jsonCountryData.flatMap(doc => [{ index: { _index: theIndex, _id: doc.id } }, doc])

	// Send data to Elasticsearch
	try {
		const { errors, items } = await esClient.bulk({ refresh: true, body: bulkOps })
		if (errors) {
			console.log('[ERROR] Bulk indexing had issues:', JSON.stringify(items, null, 2))
		} else {
			console.log(`Successfully indexed ${items.length / 2} records`)
		}
	} catch (error) {
		console.log('[ERROR] Bulk indexing failed:', error)
	}
}

indexJSON()
