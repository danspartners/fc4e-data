import { MappingTypeMapping } from 'es8/lib/api/types'

export const mappings: MappingTypeMapping = {
    properties: {
        count: {
            type: 'integer',
        },
        managers: {
            type: 'interger',
        },
        recommended_by: {
            type: 'integer',
        },
        number_of_resolvers: {
            type: 'integer',
        },
        start_date: {
            type: 'integer',
        },
		identifier_type: {
			type: 'keyword',
		},
    }
}