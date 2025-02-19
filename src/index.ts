import { esClient, initIndex } from './client'
import { mappings } from './mappings'
import fs from 'fs-extra'

const theIndex = 'fc4e'
const localJSONPath = '../data/data.json' // Path to local JSON file

export async function indexJSON() {
	await initIndex(theIndex, mappings)

	// Load JSON file
	let jsonData: any[] = []
	try {
		const fileContent = fs.readFileSync(localJSONPath, 'utf-8')
		jsonData = JSON.parse(fileContent) // Parse JSON
	} catch (error) {
		console.log('[ERROR] reading JSON file', error)
		return
	}

	console.log('Loaded JSON data:', jsonData.length, 'records')

	// // Process and index documents
	// for (const item of jsonData) {
	// 	// Normalize date formats
	// 	if (item.dates) {
	// 		for (const x of item.dates) {
	// 			if (x.date.length === 4) x.date = `${x.date}-01-01`
	// 			if (x.date.length !== 10) x.date = null
	// 		}
	// 	}
	// }
}

indexJSON()
