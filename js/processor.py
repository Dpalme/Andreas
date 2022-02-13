import csv

with open('js/output.js', 'w', encoding="UTF-8") as output:
    with open('js/Plantas_Flores.csv', 'r', encoding="UTF-8") as csv_file:
        lines = csv.reader(csv_file.readlines())
        output.write("export let plants = {\n")
        for line in lines:
            output.write('_'.join(line[0].lower().split()) + ''': {
                es: {
                    name: "''' + line[0].replace('\n', '').replace('"', '\\"') + '''",
                    info: "''' + line[2].replace('\n', '').replace('"', '\\"') + '''"
                },
                en: {
                    name: "''' + line[1].replace('\n', '').replace('"', '\\"') + '''",
                    info: "''' + line[3].replace('\n', '').replace('"', '\\"') + '''"
                },
                song: {
                    name: "''' + line[4].split('\n')[0] + '''",
                    url: "''' + line[4].split('\n')[-1] + '''"
                },
                img: {
                    src: "./img/plants/''' + '_'.join(line[0].lower().split()) + '''.jpg"
                }
            },''')
        output.write("\n}")
