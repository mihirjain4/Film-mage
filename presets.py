import os
import PIL.Image
import pilgram

def apply_inkwell(input_folder):
    if os.path.isdir(input_folder):
        for filename in os.listdir(input_folder):
            if filename.endswith(('.jpg', '.jpeg', '.png', '.JPG', '.JPEG')):
                image_path = os.path.join(input_folder, filename)
                image = PIL.Image.open(image_path)
                if not os.path.exists(os.path.join(input_folder, 'inkwell')):
                    os.makedirs(os.path.join(input_folder, 'inkwell'))
                output_path = os.path.join(input_folder, 'inkwell', 'inkwell_' + filename)
                pilgram.inkwell(image).save(output_path)
    else:
        image = PIL.Image.open(input_folder)
        output_dir = os.path.dirname(input_folder)
        output_filename = 'inkwell_' + os.path.basename(input_folder)
        output_path = os.path.join(output_dir, output_filename)
        pilgram.inkwell(image).save(output_path)


def apply_xpro(input_folder):
    if os.path.isdir(input_folder):
        for filename in os.listdir(input_folder):
            if filename.endswith(('.jpg', '.jpeg', '.png', '.JPG', '.JPEG')):
                image_path = os.path.join(input_folder, filename)
                image = PIL.Image.open(image_path)
                if not os.path.exists(os.path.join(input_folder + '/xpro')):
                    os.makedirs(os.path.join(input_folder + '/xpro'))
                output_path = os.path.join(input_folder, 'xpro', 'xpro_' + filename)
                pilgram.xpro2(image).save(output_path)
    else:
        image = PIL.Image.open(input_folder)
        output_dir = os.path.dirname(input_folder)
        output_filename = 'xpro_' + os.path.basename(input_folder)
        output_path = os.path.join(output_dir, output_filename)
        pilgram.xpro2(image).save(output_path)


def apply_aden(input_folder):
    if os.path.isdir(input_folder):
        for filename in os.listdir(input_folder):
            if filename.endswith(('.jpg', '.jpeg', '.png', '.JPG', '.JPEG')):
                image_path = os.path.join(input_folder, filename)
                image = PIL.Image.open(image_path)
                if not os.path.exists(os.path.join(input_folder + '/aden')):
                    os.makedirs(os.path.join(input_folder + '/aden'))
                output_path = os.path.join(input_folder, 'aden', 'aden_' + filename)
                pilgram.aden(image).save(output_path)
    else:
        image = PIL.Image.open(input_folder)
        output_dir = os.path.dirname(input_folder)
        output_filename = 'aden_' + os.path.basename(input_folder)
        output_path = os.path.join(output_dir, output_filename)
        pilgram.aden(image).save(output_path)


def apply_lark(input_folder):
    if os.path.isdir(input_folder):
        for filename in os.listdir(input_folder):
            if filename.endswith(('.jpg', '.jpeg', '.png', '.JPG', '.JPEG')):
                image_path = os.path.join(input_folder, filename)
                image = PIL.Image.open(image_path)
                if not os.path.exists(os.path.join(input_folder + '/lark')):
                    os.makedirs(os.path.join(input_folder + '/lark'))
                output_path = os.path.join(input_folder, 'lark', 'lark_' + filename)
                pilgram.lark(image).save(output_path)
    else:
        image = PIL.Image.open(input_folder)
        output_dir = os.path.dirname(input_folder)
        output_filename = 'lark_' + os.path.basename(input_folder)
        output_path = os.path.join(output_dir, output_filename)
        pilgram.lark(image).save(output_path)


def apply_lofi(input_folder):
    if os.path.isdir(input_folder):
        for filename in os.listdir(input_folder):
            if filename.endswith(('.jpg', '.jpeg', '.png', '.JPG', '.JPEG')):
                image_path = os.path.join(input_folder, filename)
                image = PIL.Image.open(image_path)
                if not os.path.exists(os.path.join(input_folder + '/lofi')):
                    os.makedirs(os.path.join(input_folder + '/lofi'))
                output_path = os.path.join(input_folder, 'lofi', 'lofi_' + filename)
                pilgram.lofi(image).save(output_path)
    else:
        image = PIL.Image.open(input_folder)
        output_dir = os.path.dirname(input_folder)
        output_filename = 'lofi_' + os.path.basename(input_folder)
        output_path = os.path.join(output_dir, output_filename)
        pilgram.lofi(image).save(output_path)


def apply_mayfair(input_folder):
    if os.path.isdir(input_folder):
        for filename in os.listdir(input_folder):
            if filename.endswith(('.jpg', '.jpeg', '.png', '.JPG', '.JPEG')):
                image_path = os.path.join(input_folder, filename)
                image = PIL.Image.open(image_path)
                if not os.path.exists(os.path.join(input_folder + '/mayfair')):
                    os.makedirs(os.path.join(input_folder + '/mayfair'))
                output_path = os.path.join(input_folder, 'mayfair', 'mayfair_' + filename)
                pilgram.mayfair(image).save(output_path)
    else:
        image = PIL.Image.open(input_folder)
        output_dir = os.path.dirname(input_folder)
        output_filename = 'mayfair_' + os.path.basename(input_folder)
        output_path = os.path.join(output_dir, output_filename)
        pilgram.mayfair(image).save(output_path)


def apply_gingham(input_folder):
    if os.path.isdir(input_folder):
        for filename in os.listdir(input_folder):
            if filename.endswith(('.jpg', '.jpeg', '.png', '.JPG', '.JPEG')):
                image_path = os.path.join(input_folder, filename)
                image = PIL.Image.open(image_path)
                if not os.path.exists(os.path.join(input_folder + '/gingham')):
                    os.makedirs(os.path.join(input_folder + '/gingham'))
                output_path = os.path.join(input_folder, 'gingham', 'gingham_' + filename)
                pilgram.gingham(image).save(output_path)
    else:
        image = PIL.Image.open(input_folder)
        output_dir = os.path.dirname(input_folder)
        output_filename = 'gingham_' + os.path.basename(input_folder)
        output_path = os.path.join(output_dir, output_filename)
        pilgram.gingham(image).save(output_path)


def apply_kelvin(input_folder):
    if os.path.isdir(input_folder):
        for filename in os.listdir(input_folder):
            if filename.endswith(('.jpg', '.jpeg', '.png', '.JPG', '.JPEG')):
                image_path = os.path.join(input_folder, filename)
                image = PIL.Image.open(image_path)
                if not os.path.exists(os.path.join(input_folder + '/kelvin')):
                    os.makedirs(os.path.join(input_folder + '/kelvin'))
                output_path = os.path.join(input_folder, 'kelvin', 'kelvin_' + filename)
                pilgram.kelvin(image).save(output_path)
    else:
        image = PIL.Image.open(input_folder)
        output_dir = os.path.dirname(input_folder)
        output_filename = 'kelvin_' + os.path.basename(input_folder)
        output_path = os.path.join(output_dir, output_filename)
        pilgram.kelvin(image).save(output_path)


def apply_brannan(input_folder):
    if os.path.isdir(input_folder):
        for filename in os.listdir(input_folder):
            if filename.endswith(('.jpg', '.jpeg', '.png', '.JPG', '.JPEG')):
                image_path = os.path.join(input_folder, filename)
                image = PIL.Image.open(image_path)
                if not os.path.exists(os.path.join(input_folder + '/brannan')):
                    os.makedirs(os.path.join(input_folder + '/brannan'))
                output_path = os.path.join(input_folder, 'brannan', 'brannan_' + filename)
                pilgram.brannan(image).save(output_path)
    else:
        image = PIL.Image.open(input_folder)
        output_dir = os.path.dirname(input_folder)
        output_filename = 'brannan_' + os.path.basename(input_folder)
        output_path = os.path.join(output_dir, output_filename)
        pilgram.brannan(image).save(output_path)


def apply_brooklyn(input_folder):
    if os.path.isdir(input_folder):
        for filename in os.listdir(input_folder):
            if filename.endswith(('.jpg', '.jpeg', '.png', '.JPG', '.JPEG')):
                image_path = os.path.join(input_folder, filename)
                image = PIL.Image.open(image_path)
                if not os.path.exists(os.path.join(input_folder + '/brooklyn')):
                    os.makedirs(os.path.join(input_folder + '/brooklyn'))
                output_path = os.path.join(input_folder, 'brooklyn', 'brooklyn_' + filename)
                pilgram.brooklyn(image).save(output_path)
    else:
        image = PIL.Image.open(input_folder)
        output_dir = os.path.dirname(input_folder)
        output_filename = 'brooklyn_' + os.path.basename(input_folder)
        output_path = os.path.join(output_dir, output_filename)
        pilgram.brooklyn(image).save(output_path)


def apply_earlybird(input_folder):
    if os.path.isdir(input_folder):
        for filename in os.listdir(input_folder):
            if filename.endswith(('.jpg', '.jpeg', '.png', '.JPG', '.JPEG')):
                image_path = os.path.join(input_folder, filename)
                image = PIL.Image.open(image_path)
                if not os.path.exists(os.path.join(input_folder + '/earlybird')):
                    os.makedirs(os.path.join(input_folder + '/earlybird'))
                output_path = os.path.join(input_folder, 'earlybird', 'earlybird_' + filename)
                pilgram.earlybird(image).save(output_path)
    else:
        image = PIL.Image.open(input_folder)
        output_dir = os.path.dirname(input_folder)
        output_filename = 'earlybird_' + os.path.basename(input_folder)
        output_path = os.path.join(output_dir, output_filename)
        pilgram.earlybird(image).save(output_path)


def apply_willow(input_folder):
    if os.path.isdir(input_folder):
        for filename in os.listdir(input_folder):
            if filename.endswith(('.jpg', '.jpeg', '.png', '.JPG', '.JPEG')):
                image_path = os.path.join(input_folder, filename)
                image = PIL.Image.open(image_path)
                if not os.path.exists(os.path.join(input_folder + '/willow')):
                    os.makedirs(os.path.join(input_folder + '/willow'))
                output_path = os.path.join(input_folder, 'willow', 'willow_' + filename)
                pilgram.willow(image).save(output_path)
    else:
        image = PIL.Image.open(input_folder)
        output_dir = os.path.dirname(input_folder)
        output_filename = 'willow_' + os.path.basename(input_folder)
        output_path = os.path.join(output_dir, output_filename)
        pilgram.willow(image).save(output_path)


def apply_1977(input_folder):
    if os.path.isdir(input_folder):
        for filename in os.listdir(input_folder):
            if filename.endswith(('.jpg', '.jpeg', '.png', '.JPG', '.JPEG')):
                image_path = os.path.join(input_folder, filename)
                image = PIL.Image.open(image_path)
                if not os.path.exists(os.path.join(input_folder + '/1977')):
                    os.makedirs(os.path.join(input_folder + '/1977'))
                output_path = os.path.join(input_folder, '1977', '1977_' + filename)
                pilgram._1977(image).save(output_path)
    else:
        image = PIL.Image.open(input_folder)
        output_dir = os.path.dirname(input_folder)
        output_filename = '1977_' + os.path.basename(input_folder)
        output_path = os.path.join(output_dir, output_filename)
        pilgram._1977(image).save(output_path)


def apply_rise(input_folder):
    if os.path.isdir(input_folder):
        for filename in os.listdir(input_folder):
            if filename.endswith(('.jpg', '.jpeg', '.png', '.JPG', '.JPEG')):
                image_path = os.path.join(input_folder, filename)
                image = PIL.Image.open(image_path)
                if not os.path.exists(os.path.join(input_folder + '/rise')):
                    os.makedirs(os.path.join(input_folder + '/rise'))
                output_path = os.path.join(input_folder, 'rise', 'rise_' + filename)
                pilgram.rise(image).save(output_path)
    else:
        image = PIL.Image.open(input_folder)
        output_dir = os.path.dirname(input_folder)
        output_filename = 'rise_' + os.path.basename(input_folder)
        output_path = os.path.join(output_dir, output_filename)
        pilgram.rise(image).save(output_path)


def apply_clarendon(input_folder):
    if os.path.isdir(input_folder):
        for filename in os.listdir(input_folder):
            if filename.endswith(('.jpg', '.jpeg', '.png', '.JPG', '.JPEG')):
                image_path = os.path.join(input_folder, filename)
                image = PIL.Image.open(image_path)
                if not os.path.exists(os.path.join(input_folder + '/clarendon')):
                    os.makedirs(os.path.join(input_folder + '/clarendon'))
                output_path = os.path.join(input_folder, 'clarendon', 'clarendon_' + filename)
                pilgram.clarendon(image).save(output_path)
    else:
        image = PIL.Image.open(input_folder)
        output_dir = os.path.dirname(input_folder)
        output_filename = 'clarendon_' + os.path.basename(input_folder)
        output_path = os.path.join(output_dir, output_filename)
        pilgram.clarendon(image).save(output_path)


def apply_hudson(input_folder):
    if os.path.isdir(input_folder):
        for filename in os.listdir(input_folder):
            if filename.endswith(('.jpg', '.jpeg', '.png', '.JPG', '.JPEG')):
                image_path = os.path.join(input_folder, filename)
                image = PIL.Image.open(image_path)
                if not os.path.exists(os.path.join(input_folder + '/hudson')):
                    os.makedirs(os.path.join(input_folder + '/hudson'))
                output_path = os.path.join(input_folder, 'hudson', 'hudson_' + filename)
                pilgram.hudson(image).save(output_path)
    else:
        image = PIL.Image.open(input_folder)
        output_dir = os.path.dirname(input_folder)
        output_filename = 'hudson_' + os.path.basename(input_folder)
        output_path = os.path.join(output_dir, output_filename)
        pilgram.hudson(image).save(output_path)


def apply_walden(input_folder):
    if os.path.isdir(input_folder):
        for filename in os.listdir(input_folder):
            if filename.endswith(('.jpg', '.jpeg', '.png', '.JPG', '.JPEG')):
                image_path = os.path.join(input_folder, filename)
                image = PIL.Image.open(image_path)
                if not os.path.exists(os.path.join(input_folder + '/walden')):
                    os.makedirs(os.path.join(input_folder + '/walden'))
                output_path = os.path.join(input_folder, 'walden', 'walden_' + filename)
                pilgram.walden(image).save(output_path)
    else:
        image = PIL.Image.open(input_folder)
        output_dir = os.path.dirname(input_folder)
        output_filename = 'walden_' + os.path.basename(input_folder)
        output_path = os.path.join(output_dir, output_filename)
        pilgram.walden(image).save(output_path)


def apply_maven(input_folder):
    if os.path.isdir(input_folder):
        for filename in os.listdir(input_folder):
            if filename.endswith(('.jpg', '.jpeg', '.png', '.JPG', '.JPEG')):
                image_path = os.path.join(input_folder, filename)
                image = PIL.Image.open(image_path)
                if not os.path.exists(os.path.join(input_folder + '/maven')):
                    os.makedirs(os.path.join(input_folder + '/maven'))
                output_path = os.path.join(input_folder, 'maven', 'maven_' + filename)
                pilgram.maven(image).save(output_path)
    else:
        image = PIL.Image.open(input_folder)
        output_dir = os.path.dirname(input_folder)
        output_filename = 'maven_' + os.path.basename(input_folder)
        output_path = os.path.join(output_dir, output_filename)
        pilgram.maven(image).save(output_path)


def apply_moon(input_folder):
    if os.path.isdir(input_folder):
        for filename in os.listdir(input_folder):
            if filename.endswith(('.jpg', '.jpeg', '.png', '.JPG', '.JPEG')):
                image_path = os.path.join(input_folder, filename)
                image = PIL.Image.open(image_path)
                if not os.path.exists(os.path.join(input_folder + '/moon')):
                    os.makedirs(os.path.join(input_folder + '/moon'))
                output_path = os.path.join(input_folder, 'moon', 'moon_' + filename)
                pilgram.moon(image).save(output_path)
    else:
        image = PIL.Image.open(input_folder)
        output_dir = os.path.dirname(input_folder)
        output_filename = 'moon_' + os.path.basename(input_folder)
        output_path = os.path.join(output_dir, output_filename)
        pilgram.moon(image).save(output_path)


def apply_nashville(input_folder):
    if os.path.isdir(input_folder):
        for filename in os.listdir(input_folder):
            if filename.endswith(('.jpg', '.jpeg', '.png', '.JPG', '.JPEG')):
                image_path = os.path.join(input_folder, filename)
                image = PIL.Image.open(image_path)
                if not os.path.exists(os.path.join(input_folder + '/nashville')):
                    os.makedirs(os.path.join(input_folder + '/nashville'))
                output_path = os.path.join(input_folder, 'nashville', 'nashville_' + filename)
                pilgram.nashville(image).save(output_path)
    else:
        image = PIL.Image.open(input_folder)
        output_dir = os.path.dirname(input_folder)
        output_filename = 'nashville_' + os.path.basename(input_folder)
        output_path = os.path.join(output_dir, output_filename)
        pilgram.nashville(image).save(output_path)


def apply_perpetua(input_folder):
    if os.path.isdir(input_folder):
        for filename in os.listdir(input_folder):
            if filename.endswith(('.jpg', '.jpeg', '.png', '.JPG', '.JPEG')):
                image_path = os.path.join(input_folder, filename)
                image = PIL.Image.open(image_path)
                if not os.path.exists(os.path.join(input_folder + '/perpetua')):
                    os.makedirs(os.path.join(input_folder + '/perpetua'))
                output_path = os.path.join(input_folder, 'perpetua', 'perpetua_' + filename)
                pilgram.perpetua(image).save(output_path)
    else:
        image = PIL.Image.open(input_folder)
        output_dir = os.path.dirname(input_folder)
        output_filename = 'perpetua_' + os.path.basename(input_folder)
        output_path = os.path.join(output_dir, output_filename)
        pilgram.perpetua(image).save(output_path)


def apply_reyes(input_folder):
    if os.path.isdir(input_folder):
        for filename in os.listdir(input_folder):
            if filename.endswith(('.jpg', '.jpeg', '.png', '.JPG', '.JPEG')):
                image_path = os.path.join(input_folder, filename)
                image = PIL.Image.open(image_path)
                if not os.path.exists(os.path.join(input_folder + '/reyes')):
                    os.makedirs(os.path.join(input_folder + '/reyes'))
                output_path = os.path.join(input_folder, 'reyes', 'reyes_' + filename)
                pilgram.reyes(image).save(output_path)
    else:
        image = PIL.Image.open(input_folder)
        output_dir = os.path.dirname(input_folder)
        output_filename = 'reyes_' + os.path.basename(input_folder)
        output_path = os.path.join(output_dir, output_filename)
        pilgram.reyes(image).save(output_path)


def apply_slumber(input_folder):
    if os.path.isdir(input_folder):
        for filename in os.listdir(input_folder):
            if filename.endswith(('.jpg', '.jpeg', '.png', '.JPG', '.JPEG')):
                image_path = os.path.join(input_folder, filename)
                image = PIL.Image.open(image_path)
                if not os.path.exists(os.path.join(input_folder + '/slumber')):
                    os.makedirs(os.path.join(input_folder + '/slumber'))
                output_path = os.path.join(input_folder, 'slumber', 'slumber_' + filename)
                pilgram.slumber(image).save(output_path)
    else:
        image = PIL.Image.open(input_folder)
        output_dir = os.path.dirname(input_folder)
        output_filename = 'slumber_' + os.path.basename(input_folder)
        output_path = os.path.join(output_dir, output_filename)
        pilgram.slumber(image).save(output_path)


def apply_stinson(input_folder):
    if os.path.isdir(input_folder):
        for filename in os.listdir(input_folder):
            if filename.endswith(('.jpg', '.jpeg', '.png', '.JPG', '.JPEG')):
                image_path = os.path.join(input_folder, filename)
                image = PIL.Image.open(image_path)
                if not os.path.exists(os.path.join(input_folder + '/stinson')):
                    os.makedirs(os.path.join(input_folder + '/stinson'))
                output_path = os.path.join(input_folder, 'stinson', 'stinson_' + filename)
                pilgram.stinson(image).save(output_path)
    else:
        image = PIL.Image.open(input_folder)
        output_dir = os.path.dirname(input_folder)
        output_filename = 'stinson_' + os.path.basename(input_folder)
        output_path = os.path.join(output_dir, output_filename)
        pilgram.stinson(image).save(output_path)


def apply_toaster(input_folder):
    if os.path.isdir(input_folder):
        for filename in os.listdir(input_folder):
            if filename.endswith(('.jpg', '.jpeg', '.png', '.JPG', '.JPEG')):
                image_path = os.path.join(input_folder, filename)
                image = PIL.Image.open(image_path)
                if not os.path.exists(os.path.join(input_folder + '/toaster')):
                    os.makedirs(os.path.join(input_folder + '/toaster'))
                output_path = os.path.join(input_folder, 'toaster', 'toaster_' + filename)
                pilgram.toaster(image).save(output_path)
    else:
        image = PIL.Image.open(input_folder)
        output_dir = os.path.dirname(input_folder)
        output_filename = 'toaster_' + os.path.basename(input_folder)
        output_path = os.path.join(output_dir, output_filename)
        pilgram.toaster(image).save(output_path)


def apply_valencia(input_folder):
    if os.path.isdir(input_folder):
        for filename in os.listdir(input_folder):
            if filename.endswith(('.jpg', '.jpeg', '.png', '.JPG', '.JPEG')):
                image_path = os.path.join(input_folder, filename)
                image = PIL.Image.open(image_path)
                if not os.path.exists(os.path.join(input_folder + '/valencia')):
                    os.makedirs(os.path.join(input_folder + '/valencia'))
                output_path = os.path.join(input_folder, 'valencia', 'valencia_' + filename)
                pilgram.valencia(image).save(output_path)
    else:
        image = PIL.Image.open(input_folder)
        output_dir = os.path.dirname(input_folder)
        output_filename = 'valencia_' + os.path.basename(input_folder)
        output_path = os.path.join(output_dir, output_filename)
        pilgram.valencia(image).save(output_path)


def apply_all(input_fo1der):
    apply_hudson(input_fo1der)
    apply_1977(input_fo1der)
    apply_stinson(input_fo1der)
    apply_valencia(input_fo1der)
    apply_clarendon(input_fo1der)
    apply_aden(input_fo1der)
    apply_lofi(input_fo1der)
    apply_moon(input_fo1der)
    apply_rise(input_fo1der)
    apply_xpro(input_fo1der)
    apply_inkwell(input_fo1der)
    apply_lark(input_fo1der)
    apply_maven(input_fo1der)
    apply_reyes(input_fo1der)
    apply_kelvin(input_fo1der)
    apply_walden(input_fo1der)
    apply_willow(input_fo1der)
    apply_brannan(input_fo1der)
    apply_gingham(input_fo1der)
    apply_mayfair(input_fo1der)
    apply_slumber(input_fo1der)
    apply_toaster(input_fo1der)
    apply_brooklyn(input_fo1der)
    apply_perpetua(input_fo1der)
    apply_earlybird(input_fo1der)
    apply_nashville(input_fo1der)