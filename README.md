Hej Stefan!
Action som körs när man gör någon ändring uppdaterar inte data.json fil i github, jag vet inte om det var något som vi skulle göra eller inte i uppgiften, det är därför jag välde att inte addera
den delen till min main.yml, men ifall det skulle vara något som vi måste göra, här lämnar jag exempel på koden jag skulle använda för att uppdatera data.json direkt när main.yml körs

  - name: Commit and push updates
   
    run: |
    
      git config --global user.name 'github-actions[bot]'
    
      git config --global user.email '41898282+github-actions[bot]@users.noreply.github.com'
    
      git checkout main
    
      git pull
  
      git add data.json
    
      git commit -m "Update data.json"
    
      git push origin main
