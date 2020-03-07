TAX_RATE = 0.20
STANDARD_DEDUCTION = 10000
DEPENDENT_DEDUCTION = 3000


class TaxForm():
       
       def __init__(self,grossIncome,numDependents):
              self.grossIncome = grossIncome
              self.numDependents = numDependents
       def taxableIncome(self):
              taxIncome = self.grossIncome - STANDARD_DEDUCTION - \
                     self.numDependents * DEPENDENT_DEDUCTION
              return taxIncome
       def incomeTax(self):
              incTax = TAX_RATE * self.taxableIncome()
              return incTax
