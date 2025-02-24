import { MappingTypeMapping } from 'es8/lib/api/types'

export const mappings: MappingTypeMapping = {
    properties: {
        id: { type: 'keyword' },
        api: { type: 'keyword' },
        mpa: { type: 'keyword' },
        count: { type: 'integer' },
        gupri: { type: 'keyword' },
        label: { type: 'keyword' },
        entity: { type: 'keyword' },
        scheme: { type: 'keyword' },
        status: { type: 'keyword' },
        unique: { type: 'keyword' },
        coverage: { type: 'keyword' },
        managers: { type: 'integer' },
        provider: { type: 'keyword' },
        standard: { type: 'keyword' },
        authority: { type: 'keyword' },
        countries: {
            type: 'object',
            properties: {
                name: { type: 'keyword' },
                iso: { type: 'keyword' },
                location: { type: 'geo_point' }
            }
        },
        identifier: { type: 'keyword' },
        persistent: { type: 'keyword' },
        resolvable: { type: 'keyword' },
        start_date: { 
            type: 'date',
            format: 'yyyy' 
        },
        description: { type: 'text' },
        availability: { type: 'keyword' },
        disciplinary: { type: 'keyword' },
        metaresovers: { type: 'keyword' },
        namespace_type: { type: 'keyword' },
        recommended_by: { type: 'integer' },
        globally_unique: { type: 'boolean' },
        identifier_type: { type: 'keyword' },
        resolution_type: { type: 'keyword' },
        number_of_resolvers: { type: 'integer' },
        resolution_topology: { type: 'keyword' }
    }
}
