class Solution(object):
    def splitArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def podeDividir(nums, soma_maxima, k):
            soma_atual = 0
            divisoes = 1
            for num in nums:
                if soma_atual + num > soma_maxima:
                    divisoes += 1
                    soma_atual = num
                    if divisoes > k:
                        return False
                else:
                    soma_atual += num
            return True

        esquerda, direita = max(nums), sum(nums)
        while esquerda < direita:
            meio = (esquerda + direita) // 2
            if podeDividir(nums, meio, k):
                direita = meio
            else:
                esquerda = meio + 1
        return esquerda
