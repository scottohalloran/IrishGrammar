//
//  WordClass.swift
//  IrishVocabulary
//
//  Created by Scott O'Halloran on 11/12/24.
//

import Foundation
import SwiftData

@Model

class WordClass {
    var irish = ""
    var english = ""
    var type = ""


init(irish: String, english: String, type: String) {
    self.irish = irish
    self.english = english
    self.type = type
}
    
    static let sampleData = [

        WordClass(irish: "fear", english: "man", type: "noun"),
        WordClass(irish: "bean", english: "woman", type: "noun"),
        WordClass(irish: "madra", english: "dog", type: "noun"),
        WordClass(irish: "mór", english: "big", type: "adjective"),
        WordClass(irish: "déan", english: "do", type: "verb"),

    ]
}
