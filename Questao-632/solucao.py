import heapq

class Solution(object):
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        heap = []
        maior = float('-inf')
        for i, lista in enumerate(nums):
            heapq.heappush(heap, (lista[0], i, 0))
            maior = max(maior, lista[0])
        
        menor_intervalo = float('inf')
        inicio, fim = -1, -1

        while heap:
            menor, linha, coluna = heapq.heappop(heap)
            if maior - menor < menor_intervalo:
                menor_intervalo = maior - menor
                inicio, fim = menor, maior
            
            if coluna + 1 < len(nums[linha]):
                proximo = nums[linha][coluna + 1]
                heapq.heappush(heap, (proximo, linha, coluna + 1))
                maior = max(maior, proximo)
            else:
                break
        
        return [inicio, fim]
