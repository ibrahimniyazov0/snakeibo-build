# Bu fayl Buildozer üçün AdMob kitabxanasının quraşdırılma qaydalarını müəyyən edir.

from pythonforandroid.recipe import PythonRecipe
from os.path import join

class AdMobRecipe(PythonRecipe):
    # Bu recipe'in adı olmalıdır
    name = 'kivy-admob'
    
    # Quraşdırılma tələbləri
    depends = ['python3', 'kivy']
    
    # AdMob-un native Android dependency-lərini əlavə edirik
    def get_recipe_env(self, arch):
        env = super().get_recipe_env(arch)
        # Google Play Services Ads SDK versiyasını təyin edirik
        env['REQUIRES_SDK_VERSION'] = '23.0.0'
        return env

    # Quraşdırma metodunu override edirik
    def install_python(self, arch):
        super().install_python(arch)
        # Burada hər hansı bir əlavə quraşdırma əməliyyatı yerinə yetirilə bilər
        pass

# Bu recipe-i Buildozer-a təqdim edirik
recipe = AdMobRecipe()
