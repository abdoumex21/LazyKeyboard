def main():
    from os import path
    from os import listdir
    from math import floor
    ScriptDirectory = path.dirname(path.abspath(__file__))
    UnprocessedDataFilesList = listdir(ScriptDirectory + "\\UnprocessedData")
    for File in UnprocessedDataFilesList:
        Data = []
        with open(ScriptDirectory + "\\ProcessedData\\" + File, "w") as OutputFile:
            with open(ScriptDirectory + "\\UnprocessedData\\" + File, "r") as InputFile:
                #loading data into a list of lists
                for Line in InputFile:
                    Line = Line.strip()
                    Key, Value = Line.split(" ")
                    Data.append([Key, int(Value)])
                    pass


                ValuesSum = sum(tuple([Data[i][1] for i in range(len(Data))]))
                for i in range(len(Data)):
                    Value = Data[i][1]
                    Value = Value / ValuesSum * 100
                    FlooredValue = floor(Value * 1000) / 1000 #flooring to 3 digits after the period
                    FlooringRemainder = Value - FlooredValue
                    SortingIndex = int(str(FlooringRemainder)[5:10])
                    Data[i][1] = FlooredValue
                    Data[i].append(SortingIndex)
                    pass

                Remainder = int(100 * 1000 - sum(tuple([Data[i][1] for i in range(len(Data))])) * 1000)
                Data = sorted(Data, key=lambda pair: pair[2], reverse=True) #sorting data according to the missing values from rounding 
                for i in range(Remainder):
                    Data[i][1] = round(Data[i][1] + 0.001, 3)
                    pass            
                
                for i in range(len(Data)):
                    Data[i].pop()
                    pass            
                



                Data = sorted(Data, key=lambda pair: pair[1], reverse=True) #sorting data according to the frequency 
                for i in range(len(Data)):
                    OutputFile.write(f"{Data[i][0]} {Data[i][1]}\n")

        print(f"{File} is finished")
    print("Processing Data is finished")
    return


if __name__ == "__main__":
    main()