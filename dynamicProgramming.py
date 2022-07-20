a = 'serendipitous'
b = 'precipitation'
#ans 7 reipito
#Recurtion function for finding this
def lcs(seq1,seq2):
    if seq1 == '' or seq2=='':
        return 0

    if seq1[0] == seq2[0]:
        return 1+lcs(seq1[1:], seq2[1:])
    else:
        return max(lcs(seq1[1:], seq2), lcs(seq1, seq2[1:]))

def lcs_memo(seq1,seq2):
    memo ={}
    idx1,idx2 = 0,0
    key = [idx1, idx2]
    def searching(idx1,idx2):
        if len(seq1)==idx1 or len(seq2)== idx2:
            return 0
        if key in memo:
            return memo
        elif seq1[idx1] == seq2[idx2]:
            memo[key] +=1
        else:
            memo[key] = max(searching(idx1+1,idx2), searching(idx1,idx2+1))

        return memo





print(lcs_memo(a,b))

