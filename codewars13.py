def DNA_strand(dna):
    complement = ''
    for char in dna:
        match char:
            case 'A':
                complement += 'T'
                pass
            case 'G':
                complement += 'C'
                pass
            case 'T':
                complement += 'A'
                pass
            case 'C':
                complement += 'G'
                pass
            case default:
                return " "
    return complement


print(DNA_strand('AGTC'))
