class Calculator:
    def __init__(self, operand_one: str, operand_two: str):
        self.x = int(operand_one)
        self.y = int(operand_two)

    def sum(self):
        x_list = [char for char in str(self.x).strip()]
        y_list = [char for char in str(self.y).strip()]

        if len(x_list) == 1 and len(y_list) == 1:
            return print(int(self.x) + int(self.y))

        x_list.reverse()
        y_list.reverse()

        answer = []
        carry = 0

        for i in range(len(x_list)):
            this_sum = int(x_list[i]) + int(y_list[i])

            if this_sum >= 10:
                if (i == (len(x_list) - 1)) and carry:
                    answer.append(this_sum + carry)
                else:
                    if carry:
                        answer.append(int(str(this_sum + carry)[-1]))
                        carry = int(str(this_sum)[0])
                    else:
                        answer.append(int(str(this_sum)[-1]))
                        carry = int(str(this_sum)[0])
            else:
                if carry:
                    this_sum = this_sum + carry
                    carry = 0
                    answer.append(this_sum)
                else:
                    answer.append(this_sum)

            if carry and i >= 2:
                this_sum = this_sum + carry

        answer.reverse()
        answer = ''.join(str(e) for e in answer)
        print(answer)

    def karatsuba(self):
        x = str(self.x)
        y = str(self.y)

        if len(x) < 4 and len(y) < 4:
            return print(int(x) * int(y))
        else:
            a = x[:len(x) // 2]
            b = x[len(x) // 2:]
            c = y[:len(y) // 2]
            d = y[len(y) // 2:]

            a = int(a)
            b = int(b)
            c = int(c)
            d = int(d)

            step_1 = a * c
            step_2 = b * d
            step_3 = (a + b) * (c + d)
            step_4 = (step_3 - step_2) - step_1

            answer = ((step_1 * (pow(10, 4))) + (step_4 * (pow(10, 2)))) + step_2

            return print(answer)
