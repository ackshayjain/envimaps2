from django import forms




class AddForm(forms.Form):



	title = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class':'form-control'}))

	location = forms.CharField(max_length = 100, widget=forms.TextInput(attrs={'class':'form-control'}))
	desc = forms.CharField(max_length=400, widget=forms.TextInput(attrs={'class':'form-control'}))
	pic = forms.ImageField(label="Upload Image")

	# name.widget.attrs.update({'class': 'special'})
	pic.widget.attrs.update({'class':'form-control'})
	# myfield = forms.CharField(widget=forms.TextInput(attrs={'class' : 'myfieldclass'}))

	# title = forms.CharField(max_length=200)
	# desc = forms.CharField(max_length=400)
	# location = forms.CharField(max_length = 100)
	# pic = forms.ImageField()


	# date_published = forms.DateTimeField(auto_now_add = True)
	# date_modified = forms.DateTimeField(auto_now = True)