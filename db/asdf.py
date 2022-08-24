lst = ['액션','드라마','사극','범죄', '스릴러','SF','무협','첩보','재난']

for i in lst:
    genre = Genre()
    genre.title = i
    genre.save()


Director.objects.create(name = '봉준호', debut = '1993-01-01', country = 'KOR')
Director.objects.create(name = '김한민', debut = '1999-01-01', country = 'KOR')
Director.objects.create(name = '최동훈', debut = '2004-01-01', country = 'KOR')
Director.objects.create(name = '이정재', debut = '2022-01-01', country = 'KOR')
Director.objects.create(name = '이경규', debut = '1992-01-01', country = 'KOR')
Director.objects.create(name = '한재림', debut = '2005-01-01', country = 'KOR')
Director.objects.create(name = 'Joseph Kosinski', debut = '1999-01-01', country = 'KOR')
Director.objects.create(name = '김철수', debut = '2022-01-01', country = 'KOR')

 
for i in  Director.objects.all():
    print(i.name, i.debut, i.country)
 

 
for i in Director.objects.filter(country='KOR'):
    print(i.name, i.debut, i.country)