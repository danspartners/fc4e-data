def get_location_from_iso3(iso3):
    """Fetch latitude and longitude from an ISO-3 country code."""
    return iso3_coordinates.get(iso3.upper(), None)

iso3_coordinates = {
    "ALB": {
      "lat": 41,
      "lon": 20
    },
    "DZA": {
      "lat": 28,
      "lon": 3
    },
    "ASM": {
      "lat": -14.3333,
      "lon": -170
    },
    "AND": {
      "lat": 42.5,
      "lon": 1.6
    },
    "AGO": {
      "lat": -12.5,
      "lng": 18.5
    },
    "AIA": {
      "lat": 18.25,
      "lon": -63.1667
    },
    "ATA": {
      "lat": -90,
      "lon": 0
    },
    "ATG": {
      "lat": 17.05,
      "lon": -61.8
    },
    "ARG": {
      "lat": -34,
      "lon": -64
    },
    "ARM": {
      "lat": 40,
      "lon": 45
    },
    "ABW": {
      "lat": 12.5,
      "lon": -69.9667
    },
    "AUS": {
      "lat": -27,
      "lon": 133
    },
    "AUT": {
      "lat": 47.3333,
      "lon": 13.3333
    },
    "AZE": {
      "lat": 40.5,
      "lon": 47.5
    },
    "BHS": {
      "lat": 24.25,
      "lon": -76
    },
    "BHR": {
      "lat": 26,
      "lon": 50.55
    },
    "BGD": {
      "lat": 24,
      "lon": 90
    },
    "BRB": {
      "lat": 13.1667,
      "lon": -59.5333
    },
    "BLR": {
      "lat": 53,
      "lon": 28
    },
    "BEL": {
      "lat": 50.8333,
      "lon": 4
    },
    "BLZ": {
      "lat": 17.25,
      "lon": -88.75
    },
    "BEN": {
      "lat": 9.5,
      "lon": 2.25
    },
    "BMU": {
      "lat": 32.3333,
      "lon": -64.75
    },
    "BTN": {
      "lat": 27.5,
      "lon": 90.5
    },
    "BOL": {
      "lat": -17,
      "lon": -65
    },
    "BIH": {
      "lat": 44,
      "lon": 18
    },
    "BWA": {
      "lat": -22,
      "lon": 24
    },
    "BVT": {
      "lat": -54.4333,
      "lon": 3.4
    },
    "BRA": {
      "lat": -10,
      "lon": -55
    },
    "IOT": {
      "lat": -6,
      "lon": 71.5
    },
    "BRN": {
      "lat": 4.5,
      "lon": 114.6667
    },
    "BGR": {
      "lat": 43,
      "lon": 25
    },
    "BFA": {
      "lat": 13,
      "lon": -2
    },
    "BDI": {
      "lat": -3.5,
      "lon": 30
    },
    "KHM": {
      "lat": 13,
      "lon": 105
    },
    "CMR": {
      "lat": 6,
      "lon": 12
    },
    "CAN": {
      "lat": 60,
      "lon": -95
    },
    "CPV": {
      "lat": 16,
      "lon": -24
    },
    "CYM": {
      "lat": 19.5,
      "lon": -80.5
    },
    "CAF": {
      "lat": 7,
      "lon": 21
    },
    "TCD": {
      "lat": 15,
      "lon": 19
    },
    "CHL": {
      "lat": -30,
      "lon": -71
    },
    "CHN": {
      "lat": 35,
      "lon": 105
    },
    "CXR": {
      "lat": -10.5,
      "lon": 105.6667
    },
    "CCK": {
      "lat": -12.5,
      "lon": 96.8333
    },
    "COL": {
      "lat": 4,
      "lon": -72
    },
    "COM": {
      "lat": -12.1667,
      "lon": 44.25
    },
    "COG": {
      "lat": -1,
      "lon": 15
    },
    "COD": {
      "lat": 0,
      "lon": 25
    },
    "COK": {
      "lat": -21.2333,
      "lon": -159.7667
    },
    "CRI": {
      "lat": 10,
      "lon": -84
    },
    "CIV": {
      "lat": 8,
      "lon": -5
    },
    "HRV": {
      "lat": 45.1667,
      "lon": 15.5
    },
    "CUB": {
      "lat": 21.5,
      "lon": -80
    },
    "CYP": {
      "lat": 35,
      "lon": 33
    },
    "CZE": {
      "lat": 49.75,
      "lon": 15.5
    },
    "DNK": {
      "lat": 56,
      "lon": 10
    },
    "DJI": {
      "lat": 11.5,
      "lon": 43
    },
    "DMA": {
      "lat": 15.4167,
      "lon": -61.3333
    },
    "DOM": {
      "lat": 19,
      "lon": -70.6667
    },
    "ECU": {
      "lat": -2,
      "lon": -77.5
    },
    "EGY": {
      "lat": 27,
      "lon": 30
    },
    "SLV": {
      "lat": 13.8333,
      "lon": -88.9167
    },
    "GNQ": {
      "lat": 2,
      "lon": 10
    },
    "ERI": {
      "lat": 15,
      "lon": 39
    },
    "EST": {
      "lat": 59,
      "lon": 26
    },
    "ETH": {
      "lat": 8,
      "lon": 38
    },
    "FLK": {
      "lat": -51.75,
      "lon": -59
    },
    "FRO": {
      "lat": 62,
      "lon": -7
    },
    "FJI": {
      "lat": -18,
      "lon": 175
    },
    "FIN": {
      "lat": 64,
      "lon": 26
    },
    "FRA": {
      "lat": 46,
      "lon": 2
    },
    "GUF": {
      "lat": 4,
      "lon": -53
    },
    "PYF": {
      "lat": -15,
      "lon": -140
    },
    "ATF": {
      "lat": -43,
      "lon": 67
    },
    "GAB": {
      "lat": -1,
      "lon": 11.75
    },
    "GMB": {
      "lat": 13.4667,
      "lon": -16.5667
    },
    "GEO": {
      "lat": 42,
      "lon": 43.5
    },
    "DEU": {
      "lat": 51,
      "lon": 9
    },
    "GHA": {
      "lat": 8,
      "lon": -2
    },
    "GIB": {
      "lat": 36.1833,
      "lon": -5.3667
    },
    "GRC": {
      "lat": 39,
      "lon": 22
    },
    "GRL": {
      "lat": 72,
      "lon": -40
    },
    "GRD": {
      "lat": 12.1167,
      "lon": -61.6667
    },
    "GLP": {
      "lat": 16.25,
      "lon": -61.5833
    },
    "GUM": {
      "lat": 13.4667,
      "lon": 144.7833
    },
    "GTM": {
      "lat": 15.5,
      "lon": -90.25
    },
    "GGY": {
      "lat": 49.5,
      "lon": -2.56
    },
    "GIN": {
      "lat": 11,
      "lon": -10
    },
    "GNB": {
      "lat": 12,
      "lon": -15
    },
    "GUY": {
      "lat": 5,
      "lon": -59
    },
    "HTI": {
      "lat": 19,
      "lon": -72.4167
    },
    "HMD": {
      "lat": -53.1,
      "lon": 72.5167
    },
    "VAT": {
      "lat": 41.9,
      "lon": 12.45
    },
    "HND": {
      "lat": 15,
      "lon": -86.5
    },
    "HKG": {
      "lat": 22.25,
      "lon": 114.1667
    },
    "HUN": {
      "lat": 47,
      "lon": 20
    },
    "ISL": {
      "lat": 65,
      "lon": -18
    },
    "IND": {
      "lat": 20,
      "lon": 77
    },
    "IDN": {
      "lat": -5,
      "lon": 120
    },
    "IRN": {
      "lat": 32,
      "lon": 53
    },
    "IRQ": {
      "lat": 33,
      "lon": 44
    },
    "IRL": {
      "lat": 53,
      "lon": -8
    },
    "IMN": {
      "lat": 54.23,
      "lon": -4.55
    },
    "ISR": {
      "lat": 31.5,
      "lon": 34.75
    },
    "ITA": {
      "lat": 42.8333,
      "lon": 12.8333
    },
    "JAM": {
      "lat": 18.25,
      "lon": -77.5
    },
    "JPN": {
      "lat": 36,
      "lon": 138
    },
    "JEY": {
      "lat": 49.21,
      "lon": -2.13
    },
    "JOR": {
      "lat": 31,
      "lon": 36
    },
    "KAZ": {
      "lat": 48,
      "lon": 68
    },
    "KEN": {
      "lat": 1,
      "lon": 38
    },
    "KIR": {
      "lat": 1.4167,
      "lon": 173
    },
    "PRK": {
      "lat": 40,
      "lon": 127
    },
    "KOR": {
      "lat": 37,
      "lon": 127.5
    },
    "KWT": {
      "lat": 29.3375,
      "lon": 47.6581
    },
    "KGZ": {
      "lat": 41,
      "lon": 75
    },
    "LAO": {
      "lat": 18,
      "lon": 105
    },
    "LVA": {
      "lat": 57,
      "lon": 25
    },
    "LBN": {
      "lat": 33.8333,
      "lon": 35.8333
    },
    "LSO": {
      "lat": -29.5,
      "lon": 28.5
    },
    "LBR": {
      "lat": 6.5,
      "lon": -9.5
    },
    "LBY": {
      "lat": 25,
      "lon": 17
    },
    "LIE": {
      "lat": 47.1667,
      "lon": 9.5333
    },
    "LTU": {
      "lat": 56,
      "lon": 24
    },
    "LUX": {
      "lat": 49.75,
      "lon": 6.1667
    },
    "MAC": {
      "lat": 22.1667,
      "lon": 113.55
    },
    "MKD": {
      "lat": 41.8333,
      "lon": 22
    },
    "MDG": {
      "lat": -20,
      "lon": 47
    },
    "MWI": {
      "lat": -13.5,
      "lon": 34
    },
    "MYS": {
      "lat": 2.5,
      "lon": 112.5
    },
    "MDV": {
      "lat": 3.25,
      "lon": 73
    },
    "MLI": {
      "lat": 17,
      "lon": -4
    },
    "MLT": {
      "lat": 35.8333,
      "lon": 14.5833
    },
    "MHL": {
      "lat": 9,
      "lon": 168
    },
    "MTQ": {
      "lat": 14.6667,
      "lon": -61
    },
    "MRT": {
      "lat": 20,
      "lon": -12
    },
    "MUS": {
      "lat": -20.2833,
      "lon": 57.55
    },
    "MYT": {
      "lat": -12.8333,
      "lon": 45.1667
    },
    "MEX": {
      "lat": 23,
      "lon": -102
    },
    "FSM": {
      "lat": 6.9167,
      "lon": 158.25
    },
    "MDA": {
      "lat": 47,
      "lon": 29
    },
    "MCO": {
      "lat": 43.7333,
      "lon": 7.4
    },
    "MNG": {
      "lat": 46,
      "lon": 105
    },
    "MNE": {
      "lat": 42,
      "lon": 19
    },
    "MSR": {
      "lat": 16.75,
      "lon": -62.2
    },
    "MAR": {
      "lat": 32,
      "lon": -5
    },
    "MOZ": {
      "lat": -18.25,
      "lon": 35
    },
    "MMR": {
      "lat": 22,
      "lon": 98
    },
    "NAM": {
      "lat": -22,
      "lon": 17
    },
    "NRU": {
      "lat": -0.5333,
      "lon": 166.9167
    },
    "NPL": {
      "lat": 28,
      "lon": 84
    },
    "NLD": {
      "lat": 52.5,
      "lon": 5.75
    },
    "ANT": {
      "lat": 12.25,
      "lon": -68.75
    },
    "NCL": {
      "lat": -21.5,
      "lon": 165.5
    },
    "NZL": {
      "lat": -41,
      "lon": 174
    },
    "NIC": {
      "lat": 13,
      "lon": -85
    },
    "NER": {
      "lat": 16,
      "lon": 8
    },
    "NGA": {
      "lat": 10,
      "lon": 8
    },
    "NIU": {
      "lat": -19.0333,
      "lon": -169.8667
    },
    "NFK": {
      "lat": -29.0333,
      "lon": 167.95
    },
    "MNP": {
      "lat": 15.2,
      "lon": 145.75
    },
    "NOR": {
      "lat": 62,
      "lon": 10
    },
    "OMN": {
      "lat": 21,
      "lon": 57
    },
    "PAK": {
      "lat": 30,
      "lon": 70
    },
    "PLW": {
      "lat": 7.5,
      "lon": 134.5
    },
    "PSE": {
      "lat": 32,
      "lon": 35.25
    },
    "PAN": {
      "lat": 9,
      "lon": -80
    },
    "PNG": {
      "lat": -6,
      "lon": 147
    },
    "PRY": {
      "lat": -23,
      "lon": -58
    },
    "PER": {
      "lat": -10,
      "lon": -76
    },
    "PHL": {
      "lat": 13,
      "lon": 122
    },
    "PCN": {
      "lat": -24.7,
      "lon": -127.4
    },
    "POL": {
      "lat": 52,
      "lon": 20
    },
    "PRT": {
      "lat": 39.5,
      "lon": -8
    },
    "PRI": {
      "lat": 18.25,
      "lon": -66.5
    },
    "QAT": {
      "lat": 25.5,
      "lon": 51.25
    },
    "REU": {
      "lat": -21.1,
      "lon": 55.6
    },
    "ROU": {
      "lat": 46,
      "lon": 25
    },
    "RUS": {
      "lat": 60,
      "lon": 100
    },
    "RWA": {
      "lat": -2,
      "lon": 30
    },
    "SHN": {
      "lat": -15.9333,
      "lon": -5.7
    },
    "KNA": {
      "lat": 17.3333,
      "lon": -62.75
    },
    "LCA": {
      "lat": 13.8833,
      "lon": -61.1333
    },
    "SPM": {
      "lat": 46.8333,
      "lon": -56.3333
    },
    "VCT": {
      "lat": 13.25,
      "lon": -61.2
    },
    "WSM": {
      "lat": -13.5833,
      "lon": -172.3333
    },
    "SMR": {
      "lat": 43.7667,
      "lon": 12.4167
    },
    "STP": {
      "lat": 1,
      "lon": 7
    },
    "SAU": {
      "lat": 25,
      "lon": 45
    },
    "SEN": {
      "lat": 14,
      "lon": -14
    },
    "SRB": {
      "lat": 44,
      "lon": 21
    },
    "SYC": {
      "lat": -4.5833,
      "lon": 55.6667
    },
    "SLE": {
      "lat": 8.5,
      "lon": -11.5
    },
    "SGP": {
      "lat": 1.3667,
      "lon": 103.8
    },
    "SVK": {
      "lat": 48.6667,
      "lon": 19.5
    },
    "SVN": {
      "lat": 46,
      "lon": 15
    },
    "SLB": {
      "lat": -8,
      "lon": 159
    },
    "SOM": {
      "lat": 10,
      "lon": 49
    },
    "ZAF": {
      "lat": -29,
      "lon": 24
    },
    "SGS": {
      "lat": -54.5,
      "lon": -37
    },
    "ESP": {
      "lat": 40,
      "lon": -4
    },
    "LKA": {
      "lat": 7,
      "lon": 81
    },
    "SDN": {
      "lat": 15,
      "lon": 30
    },
    "SUR": {
      "lat": 4,
      "lon": -56
    },
    "SJM": {
      "lat": 78,
      "lon": 20
    },
    "SWZ": {
      "lat": -26.5,
      "lon": 31.5
    },
    "SWE": {
      "lat": 62,
      "lon": 15
    },
    "CHE": {
      "lat": 47,
      "lon": 8
    },
    "SYR": {
      "lat": 35,
      "lon": 38
    },
    "TWN": {
      "lat": 23.5,
      "lon": 121
    },
    "TJK": {
      "lat": 39,
      "lon": 71
    },
    "TZA": {
      "lat": -6,
      "lon": 35
    },
    "THA": {
      "lat": 15,
      "lon": 100
    },
    "TLS": {
      "lat": -8.55,
      "lon": 125.5167
    },
    "TGO": {
      "lat": 8,
      "lon": 1.1667
    },
    "TKL": {
      "lat": -9,
      "lon": -172
    },
    "TON": {
      "lat": -20,
      "lon": -175
    },
    "TTO": {
      "lat": 11,
      "lon": -61
    },
    "TUN": {
      "lat": 34,
      "lon": 9
    },
    "TUR": {
      "lat": 39,
      "lon": 35
    },
    "TKM": {
      "lat": 40,
      "lon": 60
    },
    "TCA": {
      "lat": 21.75,
      "lon": -71.5833
    },
    "TUV": {
      "lat": -8,
      "lon": 178
    },
    "UGA": {
      "lat": 1,
      "lon": 32
    },
    "UKR": {
      "lat": 49,
      "lon": 32
    },
    "ARE": {
      "lat": 24,
      "lon": 54
    },
    "GBR": {
      "lat": 54,
      "lon": -2
    },
    "USA": {
      "lat": 38,
      "lon": -97
    },
    "UMI": {
      "lat": 19.2833,
      "lon": 166.6
    },
    "URY": {
      "lat": -33,
      "lon": -56
    },
    "UZB": {
      "lat": 41,
      "lon": 64
    },
    "VUT": {
      "lat": -16,
      "lon": 167
    },
    "VEN": {
      "lat": 8,
      "lon": -66
    },
    "VNM": {
      "lat": 16,
      "lon": 106
    },
    "VGB": {
      "lat": 18.5,
      "lon": -64.5
    },
    "VIR": {
      "lat": 18.3333,
      "lon": -64.8333
    },
    "WLF": {
      "lat": -13.3,
      "lon": -176.2
    },
    "ESH": {
      "lat": 24.5,
      "lon": -13
    },
    "YEM": {
      "lat": 15,
      "lon": 48
    },
    "ZMB": {
      "lat": -15,
      "lon": 30
    },
    "ZWE": {
      "lat": -20,
      "lon": 30
    },
    "AFG": {
      "lat": 33,
      "lon": 65
    }
  }