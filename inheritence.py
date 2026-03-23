class Employee {
    constructor(id, name, salary, department) {
        this.id = id;
        this.name = name;
        this.salary = salary;
        this.department = department;
    }

    // Inherited Method
    showDetails() {
        console.log("ID:", this.id);
        console.log("Name:", this.name);
        console.log("Salary:", this.salary);
        console.log("Department:", this.department);
    }

    // Method that will be overridden
    work() {
        console.log("Employee works on company tasks");
    }
}

class Developer extends Employee {

    // Overridden Method
    work() {
        console.log("Developer writes and maintains code");
    }

    // Specialized Method
    developFeature() {
        console.log("Developer develops new features");
    }
}

class Tester extends Employee {

    // Overridden Method
    work() {
        console.log("Tester tests the software");
    }

    // Specialized Method
    testApplication() {
        console.log("Tester performs application testing");
    }
}

let dev = new Developer(101, "Rahul", 80000, "Development");
let tester = new Tester(102, "Anita", 65000, "Testing");

dev.showDetails();       // inherited
dev.work();              // overridden
dev.developFeature();    // specialized

console.log("---------------");

tester.showDetails();    // inherited
tester.work();           // overridden
tester.testApplication();// specialized