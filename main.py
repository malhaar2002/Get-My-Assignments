import requests
from bs4 import BeautifulSoup

def getAssignments():
    cookies = {
        'd2lSessionVal': 't2DpQYYWLO0wbich5WnI4N12r',
        'd2lSecureSessionVal': 'hV3mI2VchjNzOmMbCSeUjbQLS',
        'ADRUM_BTa': 'R:41|g:6374ffc1-b8e4-4600-a79b-5bf74992237a|n:D2L-Prod_407a60ed-b34d-40a0-8586-bc31d0988eb7',
        'SameSite': 'None',
        'ADRUM_BT1': 'R:41|i:472144',
        'ADRUM_BTs': 'R:41|s:f',
    }

    headers = {
        'authority': 'elearning.plaksha.edu.in',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'en-US',
        'cache-control': 'max-age=0',
        # Requests sorts cookies= alphabetically
        # 'cookie': 'd2lSessionVal=t2DpQYYWLO0wbich5WnI4N12r; d2lSecureSessionVal=hV3mI2VchjNzOmMbCSeUjbQLS; ADRUM_BTa=R:41|g:6374ffc1-b8e4-4600-a79b-5bf74992237a|n:D2L-Prod_407a60ed-b34d-40a0-8586-bc31d0988eb7; SameSite=None; ADRUM_BT1=R:41|i:472144; ADRUM_BTs=R:41|s:f',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'sec-gpc': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36',
    }

    urls = {
        'Intelligent Machines': 'https://elearning.plaksha.edu.in/d2l/lms/dropbox/user/folders_list.d2l?ou=7343&isprv=0',
        'ILGC': 'https://elearning.plaksha.edu.in/d2l/lms/dropbox/user/folders_list.d2l?ou=7345&isprv=0',
        'Ethics and Communication of Technological Innovation': 'https://elearning.plaksha.edu.in/d2l/lms/dropbox/user/folders_list.d2l?ou=7344&isprv=0',
        'Electronic Systems Design': 'https://elearning.plaksha.edu.in/d2l/lms/dropbox/user/folders_list.d2l?ou=7342&isprv=0',
        'Data Science and Artificial Intelligence': 'https://elearning.plaksha.edu.in/d2l/lms/dropbox/user/folders_list.d2l?ou=7340&isprv=0',
        'Calculus in Higher Dimensions': 'https://elearning.plaksha.edu.in/d2l/lms/dropbox/user/folders_list.d2l?ou=7341&isprv=0'
    }

    assignments = {}
    index = 1

    for course in urls.keys():
        response = requests.get(urls[course], cookies=cookies, headers=headers)

        soup = BeautifulSoup(response.content, 'html.parser')

        trs = soup.find_all('tr')
        for row in trs:
            thisAssignment = {}
            try:

                # Get the assignment name and remove 'attached files' from the end
                name = row.find_all('th')[0].text
                if name.split()[-1] == 'Files':
                    name = name[:-14]
                thisAssignment['name'] = name

                # Get the course name
                thisAssignment['course'] = course

                # Get the completion status
                thisAssignment['status'] = row.find_all('td')[0].text

                # Get the due date and return empty string if due date is not set
                due = row.find_all('td')[-1].text
                if due.split()[0].isdigit() == False:
                    due = 'No due date'
                thisAssignment['due'] = due
                assignments[index] = thisAssignment

            except:
                continue
            index += 1

    return assignments