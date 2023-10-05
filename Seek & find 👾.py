import json
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

sp_json = "/Users/loukas/Desktop/Python/Cartographie Invdrs/data/space_invader"

with open(sp_json, "r") as read_file:
    data = json.load(read_file)

index_s = []
noms = []
adresses = []
coordonnees = []
latitudes = []
longitudes = []

for element in data:
    index = element["proprietes"]["index"]
    index_s.append(index)

for element in data:
    nom = element["proprietes"]["name"]
    noms.append(nom)

for element in data:
    adresse = element["proprietes"]["adresse"]
    adresses.append(adresse)

for element in data:
    latitude = element["proprietes"]["geometry"]["latitude"]
    latitudes.append(latitude)

for element in data:
    longitude = element["proprietes"]["geometry"]["longitude"]
    longitudes.append(longitude)

statuts = ["Actif" if index >= 0 else "X" for index, _ in enumerate(noms)]

df = pd.DataFrame({
    "index": index_s,
    "noms": noms,
    "adresses": adresses,
    "statut": statuts,
    "latitudes": latitudes,
    "longitudes": longitudes
})

dead_list = ["003", "020", "023", '024', '025', '026', '027', '028', '029', '030', '031', '032', '033', "034",
             "038", "039", "0237", "0254", "0266", "0267", "0309", "0428", "0485", "0534", "0616", "0653", "0892",
             "0917", "1428"]
caught_list = ['001', '002', '004', '005', '006', '007', '008', '009', '010', '011', '012', '013', '014', '015',
               '016', '017', '018', '019', '021', '022', '035', '036', '037', '040', '041', '042', "1230", "0863",
               "1409", "0118", "1296", "1033", "1336", "0371", "0811", "0944", "1014", "0415", "1054", "0369",
               "0323", "1301", "0852", "0390", "1039", "0908", "1098", "1135", "1362", "0810", "1437", "1087",
               "0874", "0392", "0121", "0880", "0630", "0176", "0592", "0322", "0635", "1167", "0183", "0180",
               "0780", "0624", "0395", "0345", "1350", "1311", "0674", "0848", "1196", "0346", "0847", "1445",
               "0941", "0365", "0901", "1208", "0934", "1272", "0626", "0364", "0247", "0347", "1429", "1044",
               "1292", "1022", "1106", "0111", "1313", "0562", "0172", "1377", "1399", "0659", "0890", "1021",
               "0656", "1020", "0690", "0418", "1382", "0533", "1372", "0336", "0989", "1018", "0329", "0990",
               "0609", "0854", "0348", "0988", "0712", "1042", "1376", "0881", "0797", "0402", "0380", "0238",
               "1253", "1254", "0236", "1101", "0821", "0535", "0829", "0871", "1186", "0494", "1315", "1122",
               "0950", "0951", "0949", "0935", "1418", "0381", "1343", "0598", "1312", "1342", "0108", "0126",
               "0343", "0344", "0968", "0966", "0967", "0666", "1061", "1393", "1391", "1415", "0779", "0786",
               "0788", "0784", "0782", "0789", "0794", "0804", "0793", "0791", "0225", "1400", "0107", "0929",
               "0426", "1191", "1192", "1193", "1195", "1199", "0942", "0875", "0303", "0079", "0056", "1103",
               "0078", "0055", "1331", "1179", "1413", "1385", "0652", "0665", "1252", "0651", "1216", "1144",
               "1143", "1112", "0876", "1108", "0272", "1134", "0706", "0422", "0385", "0527", "1240", "1104",
               "0460", "1367", "1430", "1396", "1168", "0661", "1164", "1202", "0903", "0619", "0474", "0867",
               "1280", "0660", "1406", "0726", "0995", "1410", "1394", "1398", "1462", "1114", "0439", "0728",
               "0386", "1050", "0459", "0036", "0087", "0220", "0209", "0497", "0560", "0264", "1436", "0692",
               "0695", "0691", "0693", "0762", "0259", "0922", "1205", "1038", "1411", "1223", "0258", "0478",
               "0970", "0761", "1309", "0233", "0059", "0595", "0594", "0593", "1279", "0366", "0403", "1123",
               "1447", "0405", "0646", "0897", "1306", "1387", "0915", "0543", "0837", "0718", "0465", "0999",
               "0719", "0754", "0194", "1375", "0332", "1115", "0566", "1243", "1009", "0960", "0212", "0838",
               "0715", "1027", "0717", "0832", "0834", "0835", "0822", "0827", "0461", "0610", "0119", "0771",
               "0131", "0699", "1128", "0830", "0132", "0753", "1421", "0278", "0700", "1116", "1204", "0831",
               "1149", "1158", "1142", "1242", "1226", "1225", "1451", "1133", "1224", "1183", "1121", "0515",
               "0475", "0885", "0429", "0664", "0996", "0663", "1182", "1251", "0618", "0617", "0917", "1159",
               "0268", "1004", "1160", "0178", "0476", "1294", "1073", "0449", "1074", "1310", "0918", "0862",
               "0423", "0845", "0456", "0424", "0514", "0064", "1289", "1290", "0253", "0399", "0400", "0349",
               "1249", "0331", "0525", "0273", "0092", "0720", "1432", "0327", "0062", "0606", "1299", "0455",
               "0550", "0677", "0042", "1059", "0044", "0673", "0764", "0184", "0634", "1181", "0130", "0061",
               "1057", "0427", "1458", "1340", "0976", "1008", "0755", "1322", "0756", "1229", "1269"]

for index in dead_list:
    df.loc[df['index'] == index, 'statut'] = "Dead"

for index in caught_list:
    df.loc[df['index'] == index, 'statut'] = "Caught"

counter_dead = len(dead_list)
counter_caught = len(caught_list)
counter_find = counter_dead + counter_caught

fig_map = px.scatter_mapbox(df,
                            lat="latitudes",
                            lon="longitudes",
                            hover_name="noms",
                            hover_data="adresses",
                            opacity=0.75,
                            color="statut",
                            color_discrete_sequence=["grey", "blue", "red"],
                            zoom=10,
                            title=f"Dead {counter_dead} / Caught {counter_caught} / Trouvés {counter_find}",
                            mapbox_style="carto-positron",
                            height=700)

style_de_carte = pd.DataFrame({"style": ["carto-darkmatter", "carto-positron",
                                         "open-street-map", "stamen-terrain",
                                         "stamen-toner", "stamen-watercolor",
                                         "white-bg"]})

fig_map.update_layout(margin={"r": 50, "t": 50, "l": 50, "b": 50}, )
fig_map.show()

print(df.index)

fig_table = go.Figure(data=[go.Table(
    header=dict(values=list(df.columns),
                fill_color='paleturquoise',
                align='left'),
    cells=dict(values=[df.index, df.noms, df.adresses, df.statut, df.longitudes, df.latitudes],
               fill_color='lavender',
               align='left'))
])
fig_table.show()
