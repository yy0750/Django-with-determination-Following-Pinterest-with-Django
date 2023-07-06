


class ProjectCreationForm(ModelForm):
    class Meta:
        model = Project
        fields = ['image', title', description']