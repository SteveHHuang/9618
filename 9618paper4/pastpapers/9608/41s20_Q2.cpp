#include <iostream>
using namespace std;

int MealOption1 = 0;
int MealOption2 = 0;

void MealsCount(){
    bool MoreMeals = 1;
    int MealOption;
    cout <<"Please input the option.";
    cin >> MealOption;
    if (MoreMeals){
        if (MealOption == 1){
            ++(MealOption1);
            MealsCount();
        }
        else if(MealOption == 2){
            ++(MealOption2);
            MealsCount();
        }
        else{
            cout << MealOption1 << " " << MealOption2 <<'\n';
            MoreMeals = 0;
        }

    }
    
        

}

int main(){



    return 0;
}