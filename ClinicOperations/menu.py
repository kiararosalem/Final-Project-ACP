from ClinicOperations.doctor_information import *
from ClinicOperations.patient_information import *
from ClinicOperations.medicine_list import *
from ClinicOperations.appointment_list import *

class Menu:
    def __init__(self):
        self.doc=Doctor()
        self.patient=Patient()
        self.med=Medicine_list()
        self.appoint=Appointment()

    def main_menu(self):
        while True:
            print ('-'*70)
            print("\n\t\tWelcome to Clinic Management System\n")
            print ('-'*70)
            print("\n\t\t[1] Admin Menu")
            print("\t\t[2] Patient Menu")
            print("\t\t[3] Exit")
            choice = input("\n\t\tWhere do you want to go? ")
            if choice == '1':
                self.admin_menu()
            elif choice == '2':
                self.patient_menu()
            elif choice == '3':
                exit()
            else:
                print("\n\t\tInvalid choice.") 

    def admin_menu(self):
        while True:
            print ('-'*70)
            print("\n\t\t-----Admin Menu-----\n")
            print ('-'*70)
            print("\n\t\t[1] Patient Records")
            print("\t\t[2] Doctors' Informations")
            print("\t\t[3] Medicine List")
            print("\t\t[4] Appointment List")
            print("\t\t[5] Go back to Main Menu")
            print("\t\t[6] Exit")
            choice = input("\n\t\tWhere do you want to go? ")
            if choice == '1':
                self.patient_records_menu()
            elif choice == '2':
                self.doctor_information_menu()
            elif choice == '3':
                self.medicine_menu()
            elif choice == '4':
                self.appointment_menu()
            elif choice == '5':
                return
            elif choice == '6':
                exit()
            else:
                print("\n\t\tInvalid choice.") 

    def patient_menu(self):
        while True:
            print ('-'*70)
            print("\n\t\t-----Patient Menu-----\n")
            print ('-'*70)
            print("\n\t\t[1] Make an Appointment")
            print("\t\t[2] Buy Medicine")
            print("\t\t[3] Go back to Main Menu")
            print("\t\t[4] Exit")
            choice = input("\n\t\tWhere do you want to go? ")
            if choice == '1':
                self.appoint.add_appointment()
            elif choice == '2':
                self.med.buy_medicine()
            elif choice == '3':
                return
            elif choice == '4':
                exit()
            else:
                print("\n\t\tInvalid choice.") 

    def appointment_menu(self):
        while True:
            print ('-'*70)
            print("\n\t\t-----Appointment Menu-----\n")
            print ('-'*70)
            print("\n\t\t[1] Make an Appointment")
            print("\t\t[2] Display Appointment Lists")
            print("\t\t[3] Delete Appointment")
            print("\t\t[4] Go back to Main Menu")
            print("\t\t[5] Exit")
            choice = input("\n\t\tWhere do you want to go? ")
            if choice == '1':
                self.appoint.add_appointment()
            elif choice == '2':
                self.appoint.show_appointment()
                input("\t\tPress enter to continue.")
            elif choice == '3':
                self.appoint.delete_appointment()
            elif choice == '4':
                return
            elif choice == '5':
                exit()
            else:
                print("\n\t\tInvalid choice.") 

    def patient_records_menu(self):
        while True:
            print ('-'*70)
            print("\n\t\t-----Patient Records Menu-----\n")
            print ('-'*70)
            print("\n\t\t[1] Add new Patient Record")
            print("\t\t[2] Search Patient Record")
            print("\t\t[3] View Patient Records")
            print("\t\t[4] Modify Patient Record")
            print("\t\t[5] Delete Patient Record")
            print("\t\t[6] Go back to Admin Menu")
            print("\t\t[7] Exit")
            choice = input("\n\t\tWhere do you want to go? ")
            if choice == '1':
                self.patient.add_patient()
            elif choice == '2':
                self.patient.search_patient()
            elif choice == '3':
                self.patient.show_patient_info()
                input("\t\tPress enter to continue.")
            elif choice == '4':
                self.patient.update_patient()
            elif choice == '5':
                self.patient.delete_patient()
            elif choice == '6':
                return
            elif choice == '7':
                exit()
            else:
                print("\n\t\tInvalid choice.") 

    def doctor_information_menu(self):
        while True:
            print ('-'*70)
            print("\n\t\t-----Doctor Information Menu-----\n")
            print ('-'*70)
            print("\n\t\t[1] Add new Doctor")
            print("\t\t[2] Search a Doctor")
            print("\t\t[3] View Doctor lists")
            print("\t\t[4] Modify Doctor's Information")
            print("\t\t[5] Delete Doctor's Information")
            print("\t\t[6] Go back to Admin Menu")
            print("\t\t[7] Exit")
            choice = input("\n\t\tWhere do you want to go? ")
            if choice == '1':
                self.doc.add_doctor()
            elif choice == '2':
                self.doc.search_doctor()
            elif choice == '3':
                self.doc.show_doc_info()
                input("\t\tPress enter to continue.")
            elif choice == '4':
                self.doc.update_doctor()
            elif choice == '5':
                self.doc.delete_doctor()
            elif choice == '6':
                return
            elif choice == '7':
                exit()
            else:
                print("\n\t\tInvalid choice.") 

    def medicine_menu(self):
        while True:
            print ('-'*70)
            print("\n\t\t-----Medicine Menu-----\n")
            print ('-'*70)
            print("\n\t\t[1] Add new Medicine")
            print("\t\t[2] Search a Medicine")
            print("\t\t[3] View Medicine lists")
            print("\t\t[4] Modify Medicine Information")
            print("\t\t[5] Delete Medicine Information")
            print("\t\t[6] Go back to Admin Menu")
            print("\t\t[7] Exit")
            choice = input("\n\t\tWhere do you want to go? ")
            if choice == '1':
              self.med.add_medicine()  #add
            elif choice == '2':
              self.med.search_medicine()   #search
            elif choice == '3':
                self.med.display_medicine()
                input("\t\tPress enter to continue.")   #view/display/show
            elif choice == '4':
                self.med.update_medicine()   #update/modify
            elif choice == '5':
                self.med.delete_medicine()    #delete
            elif choice == '6':
                return
            elif choice == '7':
                exit()
            else:
                print("\n\t\tInvalid choice.") 