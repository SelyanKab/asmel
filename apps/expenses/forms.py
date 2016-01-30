from django import forms

from .models import Expense

Lowner_edit_fields = ['date_purchased',
                      'month_balanced',
                      'year_balanced',
                      'expense_sum',
                      'expense_divorcee_participate',                                                                  
                      'desc',
                      'place_of_purchase',
                      'notes' ]


class ExpenseOwnerForm(forms.ModelForm):
    
    class Meta:
        model = Expense
        fields = Lowner_edit_fields
        
class ExpenseApproveForm(forms.ModelForm):
    
    class Meta:
        model = Expense
        fields = ['is_approved']    
        
        
    
        
    
    