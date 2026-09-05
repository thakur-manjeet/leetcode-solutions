class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        stack=[]
        for position,speed in cars:

            arrival_time=(target-position)/speed

            if not stack or arrival_time > stack[-1]:
                stack.append(arrival_time)

        return len(stack)        