

label update_wardrobe_lists:

### Hair Color ###
    $ wr_her_haircolor = []

    if whoring >= 0:    #brown_dye#
        $ wr_her_haircolor.append("1")
    if whoring >= 6 and "blonde_dye" in cs_existing_stock:
        $ wr_her_haircolor.append("2")
    if whoring >= 6 and "red_dye" in cs_existing_stock:
        $ wr_her_haircolor.append("3")
    if whoring >= 9 and "crimson_dye" in cs_existing_stock:
        $ wr_her_haircolor.append("4")
    if whoring >= 9 and "black_dye" in cs_existing_stock:
        $ wr_her_haircolor.append("5")

    if whoring >= 12 and "green_dye" in cs_existing_stock:
        $ wr_her_haircolor.append("6")
    if whoring >= 12 and "blue_dye" in cs_existing_stock:
        $ wr_her_haircolor.append("7")
    if whoring >= 12 and "purple_dye" in cs_existing_stock:
        $ wr_her_haircolor.append("8")
    if whoring >= 15 and "pink_dye" in cs_existing_stock:
        $ wr_her_haircolor.append("9")
    if whoring >= 18 and "white_dye" in cs_existing_stock:
        $ wr_her_haircolor.append("10")


### Tops ###
    $ wr_her_tops_uniform = [] #ADD school clothing and cheerleader tops,...

    #Uniform
    if whoring >= 0:
        $ wr_her_tops_uniform.append("uni_top_1")
    if whoring >= 3: #get right number
        $ wr_her_tops_uniform.append("uni_top_2")
    if whoring >= 6: #get right number
        $ wr_her_tops_uniform.append("uni_top_3")
    if whoring >= 9: #get right number
        $ wr_her_tops_uniform.append("uni_top_4")
    if whoring >= 12: #get right number
        $ wr_her_tops_uniform.append("uni_top_5")
    if whoring >=18:
        $ wr_her_tops_uniform.append("uni_top_6")
        $ wr_her_tops_uniform.remove("uni_top_3") #remove shirt 3. Looks ugly, no point in having it when she's willing to wear shirt 4.

    if whoring >= 3 and hg_gryffCheer_OBJ.purchased:
        $ wr_her_tops_uniform.append("uni_top_cheer_gryff")
    if whoring >= 6 and hg_gryffCheer_OBJ.purchased:
        $ wr_her_tops_uniform.append("uni_top_cheer_gryff_skimpy")

    if whoring >= 9 and hg_slythCheer_OBJ.purchased: #Add sQuest: Slytherin at heart unlock.
        $ wr_her_tops_uniform.append("uni_top_cheer_slyth")
        $ wr_her_tops_uniform.append("uni_top_cheer_slyth_skimpy")

    #Fancy
    $ wr_her_tops_fancy = []  #ADD sexy clothing
    if whoring >= 6 and "fancy_waitress_beige" in cs_existing_stock:
        $ wr_her_tops_fancy.append("fancy_waitress_beige")
    if whoring >= 9 and "fancy_waitress_green" in cs_existing_stock:
        $ wr_her_tops_fancy.append("fancy_waitress_green")

    #Wicked
    $ wr_her_tops_wicked = [] #ADD kinky clothing items like leather, fishnet
    if whoring >= 12 and "wicked_leather_jacket_short_sleeves" in cs_existing_stock:
        $ wr_her_tops_wicked.append("wicked_leather_jacket_short_sleeves")
        $ wr_her_tops_wicked.append("wicked_leather_jacket_short_sleeves_open")
    if whoring >= 12 and "wicked_leather_jacket_sleeveless" in cs_existing_stock:
        $ wr_her_tops_wicked.append("wicked_leather_jacket_sleeveless")
        $ wr_her_tops_wicked.append("wicked_leather_jacket_sleeveless_open")
    if whoring >= 12 and "wicked_leather_jacket_sleeves" in cs_existing_stock:
        $ wr_her_tops_wicked.append("wicked_leather_jacket_sleeves")
        $ wr_her_tops_wicked.append("wicked_leather_jacket_sleeves_open")

    if whoring >= 21 and hg_rocker_OBJ.purchased:
        $ wr_her_tops_wicked.append("wicked_rocker_top")

    #Muggle
    $ wr_her_tops_normal = [] #ADD Pullovers, Sweaters, Shirts, Muggle Clothing
    if whoring >= 3 and "normal_pullover" in cs_existing_stock:
        $ wr_her_tops_normal.append("normal_pullover")
        $ wr_her_tops_normal.append("normal_pullover_sexy")
    if whoring >= 6 and "normal_purple_sweater" in cs_existing_stock:
        $ wr_her_tops_normal.append("normal_purple_sweater")

    #Misc. Tops
    $ wr_her_tops_misc = []   #ADD Misc top items
    if whoring >= 9: #get right number
        $ wr_her_tops_misc.append("top_banner_gryff")
    if whoring >= 12: #get right number
        $ wr_her_tops_misc.append("top_shirt_gryff_ripped_long_tie")
        $ wr_her_tops_misc.append("top_tie_gryff")
        $ wr_her_tops_misc.append("top_banner_slyth")
    if whoring >= 18 and "top_fishnets" in cs_existing_stock:
        $ wr_her_tops_misc.append("top_fishnets")


### Bottoms ###
    $ wr_her_bottoms_uniform = [] #Page MAX=25

    #Uniform
    if whoring >= 0:
        $ wr_her_bottoms_uniform.append("uni_skirt_1")
    if whoring >= 3: #get right number
        $ wr_her_bottoms_uniform.append("uni_skirt_2")
    if whoring >= 9: #get right number
        $ wr_her_bottoms_uniform.append("uni_skirt_3")
    if whoring >= 15: #get right number
        $ wr_her_bottoms_uniform.append("uni_skirt_4")
    if whoring >= 18: #get right number
        $ wr_her_bottoms_uniform.append("uni_skirt_5")

    if whoring >= 3 and hg_gryffCheer_OBJ.purchased:
        $ wr_her_bottoms_uniform.append("uni_skirt_cheer_gryff")
    if whoring >= 9 and hg_slythCheer_OBJ.purchased: #Add sQuest: Slytherin at heart unlock.
        $ wr_her_bottoms_uniform.append("uni_skirt_cheer_slyth")

    #Uniform Low
    $ wr_her_bottoms_uniform_low = []  #Add low hanging school skirts

    if whoring >= 0:
        $ wr_her_bottoms_uniform_low.append("uni_skirt_1_low")
    if whoring >= 6:
        $ wr_her_bottoms_uniform_low.append("uni_skirt_2_low")
    if whoring >= 18: #shows panties
        $ wr_her_bottoms_uniform_low.append("uni_skirt_3_low")
    #if micro_skirt unlocked/purchased:
    #    $ wr_her_bottoms_uniform_low.append("uni_skirt_4_low") #micro skirt

    #Skirts
    $ wr_her_bottoms_skirts = [] #Add skirts
    if whoring >= 9 and "skirt_belted_mini" in cs_existing_stock:
        $ wr_her_bottoms_skirts.append("skirt_belted_mini")
    if whoring >= 18 and "skirt_belted_micro" in cs_existing_stock:
        $ wr_her_bottoms_skirts.append("skirt_belted_micro")
    #ADD japan_pant

    #Pants
    $ wr_her_bottoms_pants = [] #Add

    if "pants_jeans_long" in cs_existing_stock:
        $ wr_her_bottoms_pants.append("pants_jeans_long")
    if "pants_jeans_short" in cs_existing_stock:
        $ wr_her_bottoms_pants.append("pants_jeans_short")
    if whoring >= 18 and "pants_retro_shorts" in cs_existing_stock:
        $ wr_her_bottoms_pants.append("pants_retro_shorts")
    if whoring >= 21 and hg_rocker_OBJ.purchased:
        $ wr_her_bottoms_pants.append("pants_rocker")

    #Bottoms Misc
    $ wr_her_bottoms_misc = []   #ADD Misc bottom items

### Stockings ###

    #Neckwear
    $ wr_her_neckwears = []

    #Belts
    $ wr_her_belts = []

    #Gloves
    $ wr_her_gloves = []

    #Stockings
    $ wr_her_stockings = []

    if "stockings_gryff" in cs_existing_stock:
        $ wr_her_stockings.append("stockings_gryff")
        #if whoring  >= 21 and "vibrators" in cs_existing_stock:
        #    $ wr_her_stockings.append("stockings_gryff_vibe") #Will be in accessories instead
    if whoring >= 6 and hg_gryffCheer_OBJ.purchased:
        $ wr_her_stockings.append("stockings_gryff_cheer")
        $ wr_her_stockings.append("stockings_gryff_cheer_short")
        #if whoring  >= 21 and "vibrators" in cs_existing_stock:
        #    $ wr_her_stockings.append("stockings_gryff_cheer_vibe") #Will be in accessories instead

    if whoring >= 9 and "stockings_slyth" in cs_existing_stock: #Add sQuest: Slytherin at heart unlock.
        $ wr_her_stockings.append("stockings_slyth")
        #if whoring  >= 21 and "vibrators" in cs_existing_stock:
        #    $ wr_her_stockings.append("stockings_slyth_vibe") #Will be in accessories instead
    if whoring >= 9 and hg_slythCheer_OBJ.purchased:
        $ wr_her_stockings.append("stockings_slyth_cheer")
        $ wr_her_stockings.append("stockings_slyth_cheer_short")
        #if whoring  >= 21 and "vibrators" in cs_existing_stock:
        #    $ wr_her_stockings.append("stockings_slyth_cheer_vibe") #Will be in accessories instead
    #ADD Ravenclaw Blue. And maybe Hufflepuff.



    if "stockings_lace_black" in cs_existing_stock:
        $ wr_her_stockings.append("stockings_lace_black")

    if "stockings_fishnet_black" in cs_existing_stock:
        $ wr_her_stockings.append("stockings_fishnet_black")

    #Robes
    $ wr_her_robes = ["gryff_robe_shirt_none","gryff_robe_off"]
    if whoring >= 3:
        $ wr_her_robes.append("gryff_robe_gap_wide")
    if whoring >= 6:
        $ wr_her_robes.append("gryff_robe_seethrough")
    if whoring >= 9:
        $ wr_her_robes.append("gryff_quidditch")


    if whoring >= 6:
        $ wr_her_robes.append("slyth_robe_shirt_none")
        $ wr_her_robes.append("slyth_robe_off")
        $ wr_her_robes.append("slyth_robe_gap_wide")
    if whoring >= 9:
        $ wr_her_robes.append("slyth_robe_seethrough")
    if whoring >= 12:
        $ wr_her_robes.append("slyth_quidditch")


### Underwear ###
    $ wr_her_bras = []
    $ wr_her_bras.append("bra_white")
    $ wr_her_bras.append("bra_silk_black")
    $ wr_her_bras.append("bra_lace_turquoise")
    $ wr_her_bras.append("bra_french_maid")
    $ wr_her_bras.append("bra_bikini_string_black")
    $ wr_her_bras.append("bra_bikini_string_blue")
    $ wr_her_bras.append("bra_leather_black")

    $ wr_her_panties = []
    $ wr_her_panties.append("panties_white")
    $ wr_her_panties.append("panties_silk_black")
    $ wr_her_panties.append("panties_lace_turquoise")
    $ wr_her_panties.append("panties_french_maid")
    $ wr_her_panties.append("panties_bikini_string_black")

    $ wr_her_corsets = []

    $ wr_her_garterbelts = []

    $ wr_her_underwear_misc = []


### Outfits ###

    #Outfits
    $ wr_her_outfits = []
    $ hg_purchased_outfits = []
    if hg_maid_OBJ.purchased:
        $ wr_her_outfits.append("maid")
        $ hg_purchased_outfits.append(hg_maid_OBJ)
    if hg_gryffCheer_OBJ.purchased:
        $ wr_her_outfits.append("cheer")
        $ hg_purchased_outfits.append(hg_gryffCheer_OBJ)
    if hg_slythCheer_OBJ.purchased:
        $ wr_her_outfits.append("s_cheer")
        $ hg_purchased_outfits.append(hg_slythCheer_OBJ)
    if hg_christmas_OBJ.purchased:
        $ wr_her_outfits.append("christmas")
        $ hg_purchased_outfits.append(hg_christmas_OBJ)
    if hg_present_OBJ.purchased:
        $ wr_her_outfits.append("present")
        $ hg_purchased_outfits.append(hg_present_OBJ)
    if hg_rocker_OBJ.purchased:
        $ wr_her_outfits.append("rocker")
        $ hg_purchased_outfits.append(hg_rocker_OBJ)
    if hg_japan_OBJ.purchased:
        $ wr_her_outfits.append("japan")
        $ hg_purchased_outfits.append(hg_japan_OBJ)

    #Costumes
    $ wr_her_costumes = []
    $ hg_purchased_costumes = []
    if hg_pirate_OBJ.purchased:
        $ wr_her_costumes.append("pirate")
        $ hg_purchased_costumes.append(hg_pirate_OBJ)
    if hg_powerGirl_OBJ.purchased:
        $ wr_her_costumes.append("power")
        $ hg_purchased_costumes.append(hg_powerGirl_OBJ)
    if hg_msMarvel_OBJ.purchased:
        $ wr_her_costumes.append("marvel")
        $ hg_purchased_costumes.append(hg_msMarvel_OBJ)
    if hg_harleyQuinn_OBJ.purchased:
        $ wr_her_costumes.append("harley")
        $ hg_purchased_costumes.append(hg_harleyQuinn_OBJ)
    if hg_laraCroft_OBJ.purchased:
        $ wr_her_costumes.append("lara")
        $ hg_purchased_costumes.append(hg_laraCroft_OBJ)
    if hg_tifa_OBJ.purchased:
        $ wr_her_costumes.append("tifa")
        $ hg_purchased_costumes.append(hg_tifa_OBJ)
    if hg_witch_OBJ.purchased:
        $ wr_her_costumes.append("witch")
        $ hg_purchased_costumes.append(hg_witch_OBJ)

    #One-Pieces
    $ wr_her_onepieces = []
    $ hg_purchased_onepieces = []
    if hg_silkNightgown_OBJ.purchased:
        $ wr_her_onepieces.append("nightgown")
        $ hg_purchased_onepieces.append(hg_silkNightgown_OBJ)

    #Swimsuits
    $ wr_her_swimsuits = []
    $ hg_purchased_swimsuits = []
    #if .purchased:
    #    $ wr_her_swimsuits.append("")
    #    $ hg_purchased_swimsuits.append()

    #Dresses
    $ wr_her_dresses = []
    $ hg_purchased_dresses = []
    if hg_heartDancer_OBJ.purchased:
        $ wr_her_dresses.append("heart")
        $ hg_purchased_dresses.append(hg_heartDancer_OBJ)
    if hg_ballDress_OBJ.purchased:
        $ wr_her_dresses.append("ball_dress")
        $ hg_purchased_dresses.append(hg_ballDress_OBJ)


    ###TATTOOS
    $ wr_her_tattoo_list = []

    ###Free tattoos
    $ wr_her_tattoo_list.append("thigh/signature")

    if whoring >= 10:
        $ wr_her_tattoo_list.append("torso/twist")
        $ wr_her_tattoo_list.append("thigh/tribal")

    if whoring >= 15:
        $ wr_her_tattoo_list.append("thigh/free")

    if whoring >= 17:
        $ wr_her_tattoo_list.append("pubic/10g_raised")
        $ wr_her_tattoo_list.append("pubic/10g")
        $ wr_her_tattoo_list.append("pubic/cock_hole")
        $ wr_her_tattoo_list.append("pubic/inheat")

    if whoring >= 21:
        $ wr_her_tattoo_list.append("pubic/deatheater")
        $ wr_her_tattoo_list.append("pubic/mudblood")
        $ wr_her_tattoo_list.append("pubic/fuck_me")
        $ wr_her_tattoo_list.append("pubic/deposit")

    if whoring >= 24:
        $ wr_her_tattoo_list.append("pubic/Cumslut")
        $ wr_her_tattoo_list.append("pubic/cum_here")
        $ wr_her_tattoo_list.append("pubic/cunt")
        $ wr_her_tattoo_list.append("pubic/mudblood")
        $ wr_her_tattoo_list.append("pubic/punk_mudblood")


    return