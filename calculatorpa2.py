from graphics import *


def calc():
    win = GraphWin("calculator", 600, 600)
    win.setCoords(0.0, 0.0, 4.0, 6.0)

    digits = {}
    rectangles = []
    operators = {}

    cleaner = Rectangle(Point(0.0, 4.0), Point(1.0, 5.0))
    cleaner.draw(win)
    rectangles.append(cleaner)

    signer = Rectangle(Point(1.0, 4.0), Point(2.0, 5.0))
    signer.draw(win)
    rectangles.append(signer)

    modulus = Rectangle(Point(2.0, 4.0), Point(3.0, 5.0))
    modulus.draw(win)
    rectangles.append(modulus)
    operators.update({modulus: "%"})

    division = Rectangle(Point(3.0, 4.0), Point(4.0, 5.0))
    division.draw(win)
    rectangles.append(division)
    operators.update({division: "/"})

    seven = Rectangle(Point(0.0, 3.0), Point(1.0, 4.0))
    seven.draw(win)
    digits.update({seven: "7"})
    rectangles.append(seven)

    eight = Rectangle(Point(1.0, 3.0), Point(2.0, 4.0))
    eight.draw(win)
    digits.update({eight: "8"})
    rectangles.append(eight)

    nine = Rectangle(Point(2.0, 3.0), Point(3.0, 4.0))
    nine.draw(win)
    digits.update({nine: "9"})
    rectangles.append(nine)

    multiple = Rectangle(Point(3.0, 3.0), Point(4.0, 4.0))
    multiple.draw(win)
    rectangles.append(multiple)
    operators.update({multiple: "*"})

    four = Rectangle(Point(0.0, 2.0), Point(1.0, 3.0))
    four.draw(win)
    digits.update({four: "4"})
    rectangles.append(four)

    five = Rectangle(Point(1.0, 2.0), Point(2.0, 3.0))
    five.draw(win)
    digits.update({five: "5"})
    rectangles.append(five)

    six = Rectangle(Point(2.0, 2.0), Point(3.0, 3.0))
    six.draw(win)
    digits.update({six: "6"})
    rectangles.append(six)

    subs = Rectangle(Point(3.0, 2.0), Point(4.0, 3.0))
    subs.draw(win)
    rectangles.append(subs)
    operators.update({subs: "-"})

    one = Rectangle(Point(0.0, 1.0), Point(1.0, 2.0))
    one.draw(win)
    digits.update({one: "1"})
    rectangles.append(one)

    two = Rectangle(Point(1.0, 1.0), Point(2.0, 2.0))
    two.draw(win)
    digits.update({two: "2"})
    rectangles.append(two)

    three = Rectangle(Point(2.0, 1.0), Point(3.0, 2.0))
    three.draw(win)
    digits.update({three: "3"})
    rectangles.append(three)

    add = Rectangle(Point(3.0, 1.0), Point(4.0, 2.0))
    add.draw(win)
    rectangles.append(add)
    operators.update({add: "+"})

    zero = Rectangle(Point(0.0, 0.0), Point(2.0, 1.0))
    zero.draw(win)
    digits.update({zero: "0"})
    rectangles.append(zero)

    expo = Rectangle(Point(2.0, 0.0), Point(3.0, 1.0))
    expo.draw(win)
    rectangles.append(expo)
    operators.update({expo: "**"})

    equal = Rectangle(Point(3.0, 0.0), Point(4.0, 1.0))
    equal.draw(win)
    rectangles.append(equal)

    inputText = Entry(Point(2.0, 5.5), 20)
    inputText.setText("0")
    inputText.draw(win)
    Text(Point(0.5, 4.5), "AC").draw(win)
    Text(Point(1.5, 4.5), "+/-").draw(win)
    Text(Point(2.5, 4.5), "%").draw(win)
    Text(Point(3.5, 4.5), "/").draw(win)
    Text(Point(0.5, 3.5), "7").draw(win)
    Text(Point(1.5, 3.5), "8").draw(win)
    Text(Point(2.5, 3.5), "9").draw(win)
    Text(Point(3.5, 3.5), "x").draw(win)
    Text(Point(0.5, 2.5), "4").draw(win)
    Text(Point(1.5, 2.5), "5").draw(win)
    Text(Point(2.5, 2.5), "6").draw(win)
    Text(Point(3.5, 2.5), "-").draw(win)
    Text(Point(0.5, 1.5), "1").draw(win)
    Text(Point(1.5, 1.5), "2").draw(win)
    Text(Point(2.5, 1.5), "3").draw(win)
    Text(Point(3.5, 1.5), "+").draw(win)
    Text(Point(1.0, 0.5), "0").draw(win)
    Text(Point(2.5, 0.5), "**").draw(win)
    Text(Point(3.5, 0.5), "=").draw(win)

    num = ""
    res = ""

    while True:
        syc = False
        syc2=True
        try:
            p = win.getMouse()
        except GraphicsError:
            win.close()
            break

        for i in rectangles:
            if p.getX() >= i.getP1().getX() and p.getX() <= i.getP2().getX() and p.getY() >= i.getP1().getY() and p.getY() <= i.getP2().getY():
                con = i

        if con in digits.keys():
            for i, j in digits.items():
                if con == i:
                    num += j
                    inputText.setText(num)
            continue
        elif con in operators.keys():
            res += num

            if "+" or "%" or "/" or "*" or "**" or "-" in res:
                syc = True

                try:
                    inputText.setText(str(eval(res)))
                    num = str(eval(res))

                    res = ""
                except (SyntaxError, ZeroDivisionError):
                    inputText.setText("0")
                    num = ""
                    res = ""
                    continue

            for i, j in operators.items():
                if con == i:
                    num += j
            if syc:
                res += num
            num = ""
            continue

        elif con == equal:
            res += num
            try:
                inputText.setText(str(eval(res)))
                res = str(eval(res))
                num = ""
                num += res
                res = ""
            except (SyntaxError, ZeroDivisionError):
                num = ""
                res = ""
                inputText.setText("0")

            continue

        elif con == cleaner:
            inputText.setText("0")
            res = ""
            num = ""
            continue
        elif con == signer:
            res+=num
            if "+" or "%" or "/" or "*" or "**" or "-" in res:
                syc2=False
                try:
                    num = num[:0] + "-" + num[0:]
                    inputText.setText(str((eval(num))))
                    num=str(-(eval(res)))
                    res=""
                except (SyntaxError,ZeroDivisionError):
                    inputText.setText("0")
                    num=""
                    res=""
                    continue


            if syc2:
                res=""
                num = num[:0] + "-" + num[0:]
                inputText.setText(num)



            continue


if __name__ == "__main__":
    calc()
