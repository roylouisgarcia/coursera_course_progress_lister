#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: nostradmsx
# @Date: 2022-10-04 20:21:19
import string
import re
from types import NoneType


def main():
  specialization_with_links = [] 
  with open("coursera_in_progress_links.txt") as file:
    content = file.readlines()
  
  # find_specialization = "SPECIALIZATION"
  spec_counter = 0
  list_of_links = [] 
  name_of_course = ""
  specialization_name = ""
  for entry in content:
    specialization_result = re.search(r"^SPECIALIZATION: (.*)$", entry)
    
    if specialization_result != None:
      # Store the name of the Specialization
      specialization_name = specialization_result.group(1)
      specialization_with_links.append(specialization_name)
      # Reinitialize the list of link of courses included in the specialization
      list_of_links = []
      # Reset Course counter
      course_counter = 0
      # Increment Specialization counter 
      spec_counter += 1


    # capture the names of the links
    name_search_result = re.search(r"^Course[1-9]?[0-9]: (.*)$", entry)
    if name_search_result != None:
      name_of_course = name_search_result.group(1).strip()


    # create a list of links after identifying each specialization. Note: course link 0 is the link to the page of the specialization
    link_result = re.search(r"^link: (.*)$", entry)

    if link_result != None:
      course_link = link_result.group(1).strip()
      if course_counter != 0:
        list_of_links.append(f"{name_of_course},{course_link}")
      else:
        list_of_links.append(course_link)
      course_counter += 1
    
    line_divider_result = re.search(r"---------------------", entry)
    if line_divider_result != None:
      # print(list_of_links)
      specialization_with_links.append(list_of_links)
      
  
  with open("upper.html", "r") as UpperF:
    upper_html_content = UpperF.read()
    print(upper_html_content)

  index = 0
  course_counter = 0
  link_url = ""
  for entry in specialization_with_links:
    if index%2 == 0:
      chars = re.escape(string.punctuation)
      class_specialization_name = re.sub(r'['+chars+']', '', str({entry}).lower()).replace(" ", "_")
      print(f"<div class=\"flex-container\"><h1>{entry}</h1>")
      course_counter = 0
    else:
      for link in entry:
        link_split = link.split(",")
        if course_counter == 0:
          print(f"<a class=\"spec_link\" href=\"{link}\" target=\"_blank\">Specialization Link</a></div><div class=\"flex-container\"><ul class=\"{class_specialization_name}\">")
        else:
          link_url = link_split[1]
          done_search_result = re.search(r"^done(.*)$", link_url)

          if done_search_result != None:
            print(f"<div class=\"box done\"><li class=\"course_link\"><a href=\"{done_search_result.group(1)}\" target=\"_blank\">Course {course_counter}: {link_split[0]}</a></li></div>")
          else:
            print(f"<div class=\"box\"><li class=\"course_link\"><a href=\"{link_url}\" target=\"_blank\">Course {course_counter}: {link_split[0]}</a></li></div>")
                   
          
        course_counter +=1
      

      print("</ul></div>")  
    index += 1  


    

  with open("lower.html", "r") as LowerF:
    lower_html_content = LowerF.read()
    print(lower_html_content)






if __name__ == "__main__":
  main()
