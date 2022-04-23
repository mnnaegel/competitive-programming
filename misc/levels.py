class BST:
    def __init__(self, item, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right

    def levels(self):
        answer = []
        answer.append((1, [self.item]))

        leftresult = []
        if self.left:
            leftresult = self.left.levels()
            for i in range(len(leftresult)):
                leftresult[i] = (leftresult[i][0] + 1, leftresult[i][1])
        
        rightresult = []
        if self.right:
            rightresult = self.right.levels()
            for i in range(len(rightresult)):
                rightresult[i] = (rightresult[i][0] + 1, rightresult[i][1])
        

        for result in leftresult:
            # find the matching depth in rightresult
            for right in rightresult:
                if result[0] == right[0]:
                    for item in right[1]:
                        result[1].append(item)
                    break
        answer.extend(leftresult)

        if len(rightresult) > len(leftresult):
            answer.extend(rightresult[len(leftresult):])
        
        return answer

head = BST(90, BST(50, BST(20), BST(75)), BST(150, BST(95, BST(175))))
print(head.levels())