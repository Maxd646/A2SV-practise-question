class Solution:
    def convertTemperature(self, celsius: float) -> list[float]:
        result= []
        if celsius>=0:
            kev= celsius +273.15
            far = celsius*1.80 + 32.00
            result= [kev, far]
        return result 