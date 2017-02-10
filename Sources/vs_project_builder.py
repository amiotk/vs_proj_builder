import reader

filepaths = []
vs_xml = reader.Open('Tests/Data/test.vcxproj')
reader.Purge(vs_xml)
reader.Append_group(vs_xml, filepaths)
reader.Save(vs_xml, 'Tests/Data/out.vcxproj')
