import json

#File that contols the options

class Options():
    #Option Variables
    __OptionsTopInfoLineColor = ""

    def OptionsLoader(self):
        with open('DATA/OPTIONS/options.json', 'r') as OptionsFile:
            OptionsData = OptionsFile.read()
            OptionsData = json.loads(OptionsData)
            self.__OptionsTopInfoLineColor = str(OptionsData['options'][0]['top_info_line_color'])
            OptionsFile.close

    def GetTopInfoLineColor(self):
        return self.__OptionsTopInfoLineColor

    def ChangeTopInfoLineColor(self, newColor):
        self.__OptionsTopInfoLineColor = newColor
        #extract file contents and modify json
        with open('DATA/OPTIONS/options.json', 'r') as OptionsFile:
            OptionsData = OptionsFile.read()
            OptionsData = json.loads(OptionsData)
            OptionsData['options'][0]['top_info_line_color'] = newColor
            OptionsData = json.dumps(OptionsData)
        #delete file contents
        with open('DATA/OPTIONS/options.json', 'w') as OptionsFile:
            #write new options
            OptionsFile.write(OptionsData)
            OptionsFile.close