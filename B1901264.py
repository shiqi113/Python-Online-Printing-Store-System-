#Name:TAN SHI QI
#STUDENTID:B1901264
import math
def main():
    total_collection=0
    displayIntroductionMessage()
    name=str(input(('What is your name(<Enter to quit>):')))#press enter will end the program and show the message
    while name!='':
        photo_4R,photo_5R=getInput()
        price_4R,price_5R,total_Photo,total_Price,first_50delivery,more_50Photo,after50_delivery,cost_delivery,total=computeValues(photo_4R,photo_5R)
        printComputedValues(photo_4R,photo_5R,price_4R,price_5R,name,total_Photo,total_Price,first_50delivery,more_50Photo,after50_delivery,cost_delivery,total)
        total_collection+=total
        print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
        name=str(input('What is your name(<Enter to quit>):'))
    total=displayFinalResult(total_collection)

#function to display the introduction message
def displayIntroductionMessage():
    print('{0:^50s}'.format('<Welcome TO Crystal Clear>'))
    print('{0:^50s}'.format('=================================='))
    print('{0:^50s}'.format('**********************************'))
    print('{0:^50s}'.format('|This is an online printing store|'))
    print('{0:^50s}'.format('**********************************'))
    print('{0:^50s}'.format('=================================='))
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
    print('\tYou can choose to print in 4R or 5R size photo')
    print('\t4R size is $0.25 per print,and $0.35 for 5R')
    print('\tdelivery cost is $13.55 for the first 50 prints')
    print('\tthe subsequent charge for a group of 10 or part of is $1.75. ')
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
#function to eval the input 
def getInput():
    photo_4R,photo_5R=eval(input('Enter number of 4R followed by 5R photo to print(e.g.10,0):'))
    while photo_4R<0 or photo_5R<0:
        if(photo_4R<0 and photo_5R<0):#enter two negative input will show the message and need to input again
            print('You must enter both positive integers!')
            photo_4R,photo_5R=eval(input('Enter number of 4R followed by 5R photo to print(e.g.10,0):'))
        elif(photo_4R<0 and photo_5R>=0):#if the photo_4R is negative need to enter again
            photo_4R=eval(input('Enter the number of 4R photo :'))
        elif(photo_4R>=0 and photo_5R<0):#if the photo_5R is negative need to enter again
            photo_5R=eval(input('Enter the number of 5R photo :'))
        elif(photo_4R==0 and photo_5R<0):#if the photo_4R =0 no need to enter again
            photo_5R=eval(input('Enter the number of 5R photo :'))
        elif(photo_4R<0 or photo_5R==0):#if the photo_5R =0 no need to enter again
            photo_4R=eval(input('Enter the number of 4R photo :'))
        else:
            break
    return(photo_4R,photo_5R)

#funnction to calculate the price
def computeValues(photo_4R,photo_5R):
    price_4R=(photo_4R*0.25)
    price_5R=(photo_5R*0.35)
    total_Photo=(photo_4R+photo_5R)# calculate total photo
    total_Price=(price_4R + price_5R)# calculate total price of photo
    first_50delivery=13.55#first 50 photo delivery price
    more_50Photo=math.ceil((total_Photo-50)/10)
    after50_delivery=(more_50Photo*1.75)#after 50 photo delievery price 
    
    if(total_Photo>50):#calculate cost_delivery
        cost_delivery=first_50delivery+after50_delivery
    else:
        cost_delivery=first_50delivery
        
    total=cost_delivery+total_Price#total price
    return(price_4R,price_5R,total_Photo,total_Price,first_50delivery,more_50Photo,after50_delivery,cost_delivery,total)

#function to print the sample bill
def printComputedValues(photo_4R,photo_5R,price_4R,price_5R,name,total_Photo,total_Price,first_50delivery,more_50Photo,after50_delivery,cost_delivery,total):
     print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
     print('\nBill for {:1}'.format(name.capitalize()))
     print('---------------------------------------------')
     print(str(total_Photo) + ' photos\t\t\t\t{:.2f}'.format(total_Price))

     if(photo_4R==0 and photo_5R>0):
         print('- ' + str(photo_5R) +' 5R photos @0.35\t\t{:.2f}'.format(price_5R))
     elif(photo_4R>0 and photo_5R==0):
         print('- ' + str(photo_4R) +' 4R photos @0.25\t\t{:.2f}'.format(price_4R))
     else:
         print('- ' + str(photo_4R) +' 4R photos @0.25\t\t{:.2f}'.format(price_4R))
         print('- ' + str(photo_5R) +' 5R photos @0.35\t\t{:.2f}'.format(price_5R))
     
     if(total_Photo>50):
         print('\nDelivery cost\t\t\t\t{:.2f}'.format(cost_delivery))
         print('~ First 50 or part of:\t\t{:.2f}'.format(first_50delivery))
         print('~ ' + str(more_50Photo)+' x 10 or part of @1.75\t{:.2f}'.format(after50_delivery))
     else:
         print('\nDelivery cost\t\t\t\t{:.2f}'.format(cost_delivery))
         print('~ First 50 or part of:\t\t{:.2f}'.format(first_50delivery))

     print('---------------------------------------------')
     print('Total $\t\t\t\t\t{:.2f}'.format(total))
     print('=============================================')
#function to display final resulr          
def displayFinalResult(total_collection):
    total=0
    total+=total_collection
    if total!=0:#if total=0 will show no transaction
        print('Total collection:${:.2f}'.format(total_collection))
    else:
        print('No transaction for the day')
main()
