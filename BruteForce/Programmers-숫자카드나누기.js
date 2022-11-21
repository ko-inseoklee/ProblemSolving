function solution(arrayA, arrayB) {
  arrayA = arrayA.sort((a,b) => a - b);
  arrayB = arrayB.sort((a,b) => a - b);
  
  let solutionA = [], solutionB = [];
  
  for(let i = 2; i <= arrayA[0]; i++){
      for (let j = 0; j < arrayA.length; j++) {
          if (arrayA[j] % i !== 0) break;
          else if (j === arrayA.length - 1) solutionA.push(i);
          else continue;
      }
  }
      
  for(let i = 2; i <= arrayB[0]; i++){
      for (let j = 0; j < arrayB.length; j++) {
          if (arrayB[j] % i !== 0) break;
          else if (j === arrayB.length - 1) solutionB.push(i);
          else continue;
      }
  }
  
  let solution = [];
  
  for(let i = 0; i < solutionA.length; i++){
      for (let j = 0; j < arrayB.length; j++){
          if (arrayB[j] % solutionA[i] === 0) break;
          else if (j === arrayB.length - 1) solution.push(solutionA[i]);
          else continue;
      }
  }
  
  for(let i = 0; i < solutionB.length; i++){
      for (let j = 0; j < arrayA.length; j++){
          if (arrayA[j] % solutionB[i] === 0) break;
          else if (j === arrayA.length - 1) solution.push(solutionB[i]);
          else continue;
      }
  }
      
  if (solution.length === 0) return 0;
  else {
      solution.sort((a,b) => a - b);
      return solution[solution.length - 1];
  }
}