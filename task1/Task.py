from argparse import ArgumentParser
from matplotlib import pyplot, axes, patches
from LinearFunction import LinearFunction
import pandas

def showData(data : pandas.DataFrame):
    print(data.describe(percentiles=[]).drop(["std", "50%"]))
    print()

def getXYValues(data : pandas.DataFrame, xRow : str, yRow : str) -> tuple[list, list]:
    data = dataFrame[[xRow, yRow]].T.values
    x = data[0]
    y = data[1]
    return (x, y)

def fillDots(axes : axes.Axes, xData, yData):
    axes.plot(xData, yData, "o", color="r")

def fillDotsAndLine(axes : axes.Axes, xData, yData, function : LinearFunction):
    fillDots(axes, xData, yData)
    lineX = [min(xData), max(xData)]
    lineY = [function(lineX[0]), function(lineX[1])]

    axes.plot(lineX, lineY, color="b")

def fillDotsAndLineAndErrorSquares(axes : axes.Axes, xData, yData, function : LinearFunction):
    fillDotsAndLine(axes, xData, yData, function)
    for i in range(len(xData)):
        x = xData[i]
        y = yData[i]
        approtimatedY = function(x)

        squareSize = approtimatedY - y
        rectanglePatch = patches.Rectangle((x, y), -squareSize, squareSize, fill=False, hatch="////")
        axes.add_patch(rectanglePatch)


parser = ArgumentParser()
parser.add_argument("--file", type=str, default="Task1\\student_scores.csv", help="File to analyze")
parser.add_argument("--xRow", type=str, default="Hours", help="X row on graph")
parser.add_argument("--yRow", type=str, default="Scores", help="Y row on graph")
args = parser.parse_args()


dataFrame = pandas.read_csv(args.file)
showData(dataFrame)
(x, y) = getXYValues(dataFrame, args.xRow, args.yRow)
fig, (axis1, axis2, axis3) =  pyplot.subplots(3)

functionApproximation = LinearFunction.FindApproximatedLinearFunction(x, y)

fillDots(axis1, x, y)
fillDotsAndLine(axis2, x, y, functionApproximation)
fillDotsAndLineAndErrorSquares(axis3, x, y, functionApproximation)
pyplot.show()