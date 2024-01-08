import pickle
import os

class IconHashMap:
    def __init__(self):
        self.image_dict = {}
        self.next_id = 1

    def addImage(self, image_name):
        if image_name not in self.image_dict:
            self.image_dict[self.next_id] = image_name
            self.next_id += 1

    def getName(self, image_id):
        return self.image_dict.get(image_id, None)

    def getAllIds(self):
        return list(self.image_dict.keys())

    def saveToFile(self, file_path):
        with open(file_path, 'wb') as file:
            pickle.dump(self.image_dict, file)

    def loadFromFile(self, file_path="./image_hash_map.pkl"):
        with open(file_path, 'rb') as file:
            self.image_dict = pickle.load(file)

    def _getIconNames(self, folder_path):
        try:
            # Get all files in the folder
            files = os.listdir(folder_path)
            # Filter only image files (you can customize the extensions)
            image_files = [file for file in files if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]

            return image_files
        except Exception as e:
            print(f"Error: {e}")
            return []

    def refreshHash(self, folderPath="./icons"):
        self._folderPath = folderPath
        # Get the image names
        iconLists = self._getIconNames(self._folderPath)
        for i, imageName in enumerate(iconLists):
            self.addImage(imageName)
            print(f"Image Name: {imageName}, Unique ID: {i+1}")
            
        # Save the hash map to a file
        self.saveToFile("image_hash_map.pkl")