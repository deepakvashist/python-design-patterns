class PrimeFinder:

    def __init__(self):
        self.primes = []

    def calculate(self, limit):
        pass

    def out(self):
        print(self.__class__.__name__)
        for prime in self.primes:
            print(prime)


class HardCodedPrimeFinder(PrimeFinder):

    def calculate(self, limit):
        hardcoded_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43]
        for prime in hardcoded_primes:
            if prime < limit:
                self.primes.append(prime)


class StandardPrimeFinder(PrimeFinder):

    def calculate(self, limit):
        self.primes = [2]
        for number in range(3, limit, 2):
            is_prime = True
            for prime in self.primes:
                if number % prime == 0:
                    is_prime = False
                    break
            if is_prime:
                self.primes.append(number)


class PrimeFinderClient:

    def __init__(self, limit):
        self.limit = limit
        if limit <= 50:
            self.finder = HardCodedPrimeFinder()
        else:
            self.finder = StandardPrimeFinder()

    def get_primes(self):
        self.finder.calculate(self.limit)
        self.finder.out()


if __name__ == '__main__':
    prime = PrimeFinderClient(50)
    prime.get_primes()
    prime = PrimeFinderClient(100)
    prime.get_primes()
