def avg_score(a) :
    if len(a) > 0 :
       total = a.values()
       total_sum = sum(total)
       total_avg = total_sum / len(a)
       return total_avg
    else :
        return None



scores = {"kim" : 95,"lee": 65,}
avg = avg_score(scores)


if avg != None : 
    print(f"평균{avg}")
else : 
    print("점수가없음")
