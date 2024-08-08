path = '/content/drive'
drive_path = path + '/MyDrive/minecraft_server'

r = get('https://raw.githubusercontent.com/N-aksif-N/MineColab_Improved/app/update.txt')
if 'update=True' in r.text or exists(path + '/MyDrive/streamlit-app') == False:
  r = get('https://github.com/N-aksif-N/MineColab_Improved/archive/refs/heads/app.zip')
  with open('/content/app.zip', 'wb') as f:
    f.write(r.content)
  with ZipFile('/content/app.zip', 'r') as zip_ref:
    zip_ref.extractall(path='/content')
  if exists(path + '/MyDrive/streamlit-app'):
    if exists(f'{path}/MyDrive/streamlit-app/user.txt'):
      move(f'{path}/MyDrive/streamlit-app/user.txt', '/content/user.txt')
      sleep(5)
    rmtree(path + '/MyDrive/streamlit-app')
    sleep(5)
  move('/content/MineColab_Improved-app/streamlit-app', f'{path}/MyDrive')
  if exists('/content/user.txt'):
    remove(f'{path}/MyDrive/streamlit-app/user.txt')
    move('/content/user.txt', f'{path}/MyDrive/streamlit-app')
  sleep(10)
  remove('/content/app.zip')
  rmtree('/content/MineColab_Improved-app')
  sleep(5)
  dump({'choose': True, 'user': {'authtoken': ''}}, open(path + '/MyDrive/streamlit-app/user.txt', 'w'))
  # Creating minecraft_server folder
  sleep(10)
  if exists(drive_path) == False:
    makedirs(drive_path)
    makedirs(f'{drive_path}/logs')
  if exists(f'{drive_path}/serverconfig.txt') == False:
    dump({"server_list": [], "ngrok_proxy" : {"authtoken" : '', "region" : ''}, "zrok_proxy": {"authtoken": ''}, "localtonet_proxy": {"authtoken": ''}}, open(drive_path + '/serverconfig.txt', 'w'))
sleep(20)
