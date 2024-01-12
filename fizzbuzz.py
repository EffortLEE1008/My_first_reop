def do_fizzbuzz():
    for i in ragne(1,15+1):

        if i%3==0 or i%5 :
            print('fizz'*(i%3==0)+'buzz'*(i%5==0))
        
        else :
            print(f'{i}')



if __name__=='__main__':
    do_fizzbuzz()



