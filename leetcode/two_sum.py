#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.

class Solution(object):
    def twosum(self, nums, target):

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
                else:
                    err_message = print('There is no numbers to get equal to the target')
                    return err_message

'''if __name__ == '__main__':
    s = Solution()
    print(s.twosum(nums=[2, 7, 11, 15], target=8))'''

'''Another solution given by AI help. Better solution '''


class Solution(object):
    def twoSum(self, nums, target):
        memoria = {}
        for i, num in enumerate(nums):
            complemento = target - num
            if complemento in memoria:
                return [memoria[complemento], i]
            memoria[num] = i
        return []  # Por si no encuentra nada


# 2. El bloque de ejecución (Esto es lo nuevo)
if __name__ == "__main__":
    # Creamos un objeto de la clase Solution
    solucionador = Solution()

    # Definimos datos de prueba
    mis_numeros = [3, 5, 8, 11, 1, 2]
    mi_objetivo = 6

    # Llamamos a la función y guardamos el resultado
    resultado = solucionador.twoSum(mis_numeros, mi_objetivo)

    # Imprimimos para ver que funcione
    print(f"Los índices son: {resultado}")