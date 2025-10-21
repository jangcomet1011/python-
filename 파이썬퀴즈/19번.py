def avg_score(a) :
    if len(a) > 0 :
        total = 0
        total_key = 0
        for key, score in a.items() :
            total = total + score
            total_key
        total_avg = total / len(a)
        return total_avg
    else :
        return None



scores = {"kim" : 95,"lee": 65,}
avg = avg_score(scores)


if avg != None : 
    print(f"평균{avg}")
else : 
    print("점수가없음")
