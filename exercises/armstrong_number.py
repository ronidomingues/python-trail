class ArmstrongNumber:
    """
        Esta classe foi criada para verificar se um número inteiro dado é um número de Armstrong.
        O que é o número de Armstrong?
        É um número inteiro em que este é igual a soma dos seus próprios digitos, cada um elevado a potência
        do numero total de digitos que este possui, por exemplo o número 153 = 1^3 + 5^3 + 3^3 = 153.
        Ou seja, dado um número inteiro X com n dígitos, este será um número de Armstrong se, e somente se
        X igual a soma de cada um de seus dígitos elevados e a n-ésima potência um a um.
        X é um número de Armstrong para n = 3 se: X = C(X)^3 + D(X)^3 + U(X)^3, onde C, D, U são respectivamente
        as casas da Centena, Dezena e Unidade do número X.
        Por fim um número de Armstrong é um número que é igual à soma de seus dígitos elevados à potência do número de dígitos.
    """
    def __init__(self:object, number: int = 153) -> None:
        self.number = number
        self.number_str = str(number) # Converte o número para string para facilitar na iteração sobre seus dígitos;
        self.lengh = len(self.number_str) # Armazena o número de dígitos do número;
    def is_armstrong_number(self: object) -> bool:
        sum_digit = 0
        for digit in self.number_str:
            sum_digit += (int(digit)) ** (self.lengh)
        print(sum_digit == self.number)
        return sum_digit == self.number
    def first_armstrong_number_between(self: object) -> list:
        pass
#
if __name__ == "__main__":
    new_test = ArmstrongNumber()
    new_test.is_armstrong_number()
