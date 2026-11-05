package example;

/* metamodel_version: 1.12.0 */
/* version: 1.0, 1.1-rc3 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  A FIX field: its tag number, name, datatype or code set, and the limits on its value.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OrchestraFieldV10  {

  private List<OrchestraFieldRuleV10> fixrRule;
  private String fixrAssign;
  private OrchestraAnnotationV10 fixrAnnotation;
  private String fixrType;
  private Integer fixrLengthId;
  private Integer fixrDiscriminatorId;
  private String fixrBaseCategory;
  private String fixrBaseCategoryAbbrName;
  private String fixrUnionDataType;
  private int fixrId;
  private String fixrName;
  private String fixrAbbrName;
  private String fixrScenario;
  private String fixrAdded;
  private Integer fixrAddedEp;
  private String fixrChangeType;
  private String fixrDeprecated;
  private Integer fixrDeprecatedEp;
  private String fixrIssue;
  private String fixrLastModified;
  private String fixrReplaced;
  private Integer fixrReplacedEp;
  private Integer fixrReplacedByField;
  private String fixrSupported;
  private String fixrUpdated;
  private Integer fixrUpdatedEp;
  private String fixrMinInclusive;
  private String fixrMaxInclusive;
  private Integer fixrImplLength;
  private Integer fixrImplMinLength;
  private Integer fixrImplMaxLength;
  private String fixrPresence;
  private String fixrEncoding;
  private String fixrValue;
  private String fixrRendering;


}