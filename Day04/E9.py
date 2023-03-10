# 9.	Cut(slice) out the first word of Coding For All string.
company = 'Coding for All'
companyPieces = company.split()
company = ''
for i in range(1,len(companyPieces)):
    company += companyPieces[i]+' '

print(company)