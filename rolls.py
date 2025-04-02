#Imports below:
import dice
import robyn

#Saving Throws (I believe this should use d20 instead of d12+d8, but I should confirm)
strength_throw = dice.randomer_d20 + robyn.strength_modifier + robyn.strength_save
dexterity_throw = dice.randomer_d20 + robyn.dexterity_modifier + robyn.dexterity_save
constitution_throw = dice.randomer_d20 + robyn.constitution_modifier + robyn.constitution_save
intelligence_throw = dice.randomer_d20 + robyn.intelligence_modifier + robyn.intelligence_save
wisdom_throw = dice.randomer_d20 + robyn.wisdom_modifier + robyn.wisdom_save
charisma_throw = dice.randomer_d20 + robyn.charisma_modifier + robyn.charisma_save

#Ability Checks
strength_check = dice.randomer_d12 + dice.randomer_d8 + robyn.strength_modifier
dexterity_check = dice.randomer_d12 + dice.randomer_d8 + robyn.dexterity_modifier
constitution_check = dice.randomer_d12 + dice.randomer_d8 + robyn.constitution_modifier
intelligence_check = dice.randomer_d12 + dice.randomer_d8 + robyn.intelligence_modifier
wisdom_check = dice.randomer_d12 + dice.randomer_d8 + robyn.wisdom_modifier
charisma_check = dice.randomer_d12 + dice.randomer_d8 + robyn.charisma_modifier

#Skill Checks
acrobatics_check = dexterity_check + robyn.acrobatics
animal_handling_check = wisdom_check + robyn.animal_handling
arcana_check = intelligence_check + robyn.arcana
athletics_check = strength_check + robyn.athletics
deception_check = charisma_check + robyn.deception
history_check = intelligence_check + robyn.history
insight_check = wisdom_check + robyn.insight
intimidation_check = charisma_check + robyn.intimidation
investigation_check = intelligence_check + robyn.investigation
medicine_check = wisdom_check + robyn.medicine
nature_check = intelligence_check + robyn.nature
perception_check = wisdom_check + robyn.perception
performance_check = charisma_check + robyn.performance
persuasion_check = charisma_check + robyn.persuasion
religion_check = intelligence_check + robyn.religion
sleight_of_hand_check = dexterity_check + robyn.sleight_of_hand
stealth_check = dexterity_check + robyn.stealth
survival_check = wisdom_check + robyn.survival

#Attack Rolls
agonizing_eldritch_attack = dice.randomer_d20 + robyn.charisma_modifier + robyn.proficiency_bonus
main_dagger_attack = dice.randomer_d20 + robyn.dexterity_modifier + robyn.proficiency_bonus
off_dagger_attack = dice.randomer_d20 + robyn.dexterity_modifier + robyn.proficiency_bonus
main_shadow_blade_attack = dice.randomer_d20 + robyn.dexterity_modifier + robyn.proficiency_bonus
off_shadow_blade_attack = dice.randomer_d20 + robyn.dexterity_modifier + robyn.proficiency_bonus
main_light_hammer_attack = dice.randomer_d20 + robyn.strength_modifier + robyn.proficiency_bonus
off_light_hammer_attack = dice.randomer_d20 + robyn.strength_modifier + robyn.proficiency_bonus
light_crossbow_attack = dice.randomer_d20 + robyn.dexterity_modifier + robyn.proficiency_bonus

#Attack Damage
agonizing_eldritch_damage = dice.randomer_d10 + robyn.charisma_modifier
main_dagger_damage = dice.randomer_d4 + robyn.dexterity_modifier
off_dagger_damage = dice.randomer_d4
main_shadow_blade_damage = sum(dice.randomer_fct_d8() for _ in range(2)) + robyn.dexterity_modifier
off_shadow_blade_damage = sum(dice.randomer_fct_d8() for _ in range(2))
main_light_hammer_damage = dice.randomer_d4 + robyn.strength_modifier
off_light_hammer_damage = dice.randomer_d4
light_crossbow_damage = dice.randomer_d8 + robyn.dexterity_modifier
sacred_flame_damage = dice.randomer_d8
hel_ish_rebuke_damage = sum(dice.randomer_fct_d10() for _ in range(3))

#Healing Hit Points (all dice is controversial, particularly for healing light as it is max 4)
short_rest_hit_dice = dice.randomer_d8 + robyn.constitution_modifier
all_short_rest_hit_dice = sum((dice.randomer_fct_d8() + robyn.constitution_modifier) for _ in range(robyn.level))
healing_light_dice = dice.randomer_d6
max_healing_light_dice = sum(dice.randomer_fct_d6() for _ in range(robyn.charisma_modifier))

#Fearful Symmetry Talisman
talisman_ability_check_buff = dice.randomer_d4