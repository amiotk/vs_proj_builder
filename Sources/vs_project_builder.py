import vsproj

filepaths = []
vs_xml = vsproj.Open('Tests/Data/test.vcxproj')
vsproj.Purge(vs_xml)
vsproj.Append_group(vs_xml, filepaths)
vsproj.Save(vs_xml, 'Tests/Data/out.vcxproj')
