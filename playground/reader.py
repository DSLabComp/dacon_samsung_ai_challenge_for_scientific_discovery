def readSDF(filename):
    f = open(filename, 'r')
    file_lines = f.read()
    f.close()
    
    file_lines = file_lines.split("$$$$")
    
    output_list = []
    
    for molecule_item in file_lines:
        molecule_item = molecule_item.split('> <')
        temp_item_output = {}
        i = 0
        for molecule_property in molecule_item:
            if i == 0:
                temp_item_output['MDL'] = molecule_property.strip()
            else:
                molecule_property = molecule_property.split("\n")
                property_key = ''
                property_value = []
                j = 0
                for molecule_property_line in molecule_property:
                    if j == 0:
                        property_key = molecule_property_line.strip()[:-1]
                    else:
                        property_value.append(molecule_property_line)
                    j = j + 1
                property_value = "\n".join(property_value).strip()
                temp_item_output[property_key] = property_value
            i = i + 1
        output_list.append(temp_item_output)
    
    return output_list


print(readSDF("train_0.sdf"))

