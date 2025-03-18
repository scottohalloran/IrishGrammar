//
//  WordListClass.swift
//  IrishVocabulary
//
//  Created by Scott O'Halloran on 11/12/24.
//

import Foundation
import SwiftData

@Model


class WordListClass {
    var name = ""
    var words = [WordClass]()
 
    init(name: String, words: [WordClass]) {
        self.name = name
        self.words = words
        
    }
    
    static let sampleData = [

        WordListClass( name: "List1", words: [WordClass(irish: "fear", english: "man", type: "noun"),
            WordClass(irish: "bean", english: "woman", type: "noun"),
            WordClass(irish: "madra", english: "dog", type: "noun"),
            WordClass(irish: "mór", english: "big", type: "adjective"),
            WordClass(irish: "déan", english: "do", type: "verb"),])


    ]
}
