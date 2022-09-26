function solution(n, times) {
    var answer = 0;

    times.sort(); 
    
    //right 범위 설정(최대 심사인원 * 최대 입국심사 시간)
    var right = times[times.length-1] * n;
    var left = 1;
    
    while(left < right){
        var mid = Math.floor((left + right) / 2);
        
        var tmpTime = 0;
        for(let i = 0; i < times.length; i++){
            tmpTime += Math.floor(mid / times[i]);
            if(tmpTime >= n) break;
        }
        if (tmpTime >= n) {
            right = mid;
        }
        else left = mid + 1;
    }
    
    answer = right;

    return answer;
}