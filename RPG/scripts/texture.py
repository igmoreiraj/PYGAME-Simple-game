import pygame

pygame.init()




class Tiles:

    Size = 32

    Blocked=[]

    Blocked_Types=["3","6", "7", "8"]

    def Blocked_At(pos):
        if list(pos) in Tiles.Blocked:
            return True
        else:
            return False
    
    def Load_Texture(file,Size):
        bitmap=pygame.image.load(file)
        bitmap=pygame.transform.scale(bitmap,(Size,Size))
        surface = pygame.Surface((Size,Size),pygame.HWSURFACE|pygame.SRCALPHA)
        surface.blit(bitmap,(0,0))
        return surface

    Grass = Load_Texture("graphics\\grass.png",Size)

    Stone = Load_Texture("graphics\\stone.png",Size)

    Water = Load_Texture("graphics\\water.png",Size)

    Caminho = Load_Texture("graphics\\caminho.png",Size)

    deserto = Load_Texture("graphics\\deserto.png",Size)

    pedra = Load_Texture("graphics\\pedra.png",Size)

    tree = Load_Texture("graphics\\tree.png",Size)

    montanha = Load_Texture("graphics\\montanha.png",Size)


    Texture_Tags={"1" : Grass, "2" : Stone, "3" : Water, "4" : Caminho,
                  "5": deserto, "6" : pedra, "7" : tree, "8" : montanha}
