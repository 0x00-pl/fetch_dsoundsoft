import re

def main(filename):
  txt = open(filename).read()
  link_list = re.findall("/voice/info/[^\"]+", txt)
  link_list = list(set(link_list))
  name_list = [i[len("/voice/info/"):] for i in link_list]
  base_url = 'http://www.dsoundsoft.com/voice/download/'
  download_page_list = [base_url+i for i in name_list]
  print('\n'.join(download_page_list))


if __name__=='__main__':
  main('html_voice.txt')
