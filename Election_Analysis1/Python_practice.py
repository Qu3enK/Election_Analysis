print('Hello World')
counties = []
counties.append('El Paso')
print(counties)
counties.insert(0, 'Pitt')
print(counties)
counties_tuple = ('Arapahoe', 'Dever', 'Jefferson')
print(counties_tuple)
print(counties_tuple[:-1])
print('-------------------')
voting_data =[]
voting_data.append({'county':'Arapahoe','registered_voters':422829})
voting_data.append({'county':'Dever','registered_voters':463353})
voting_data.append({'county':'Jefferson', 'registered_voters':432438})
print(voting_data)
print('-----orig list-----------')
voting_data.append({'county':'El Paso','registered_voters':461149})
print(voting_data)
print('------add el paso----------')
voting_data.remove({"county":"Arapahoe", "registered_voters": 422829})
print(voting_data)
print('------remove arapahoe-----')
